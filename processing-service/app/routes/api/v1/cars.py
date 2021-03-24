from app.database.models.car_image import CarImage
from app.database.models.image import Image
from app.database.models.make_alias import MakeAlias
import json
import re
from datetime import date, datetime

import requests
from app.database.models.car import BodyType, CarSchema, DriveType, FuelType, TransmissionType
from bs4 import BeautifulSoup, Tag
from flask_restplus import Resource, fields, abort

from ....database.db import db
from ....database.models import Car
from ....database.models.make import Make
from ....helpers import snake_case_keys
from .api import api


def get_car_data(url):
    if url.startswith("https://www.carforyou.ch"):
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        script = soup.find(id="__NEXT_DATA__")
        contents = script.contents[0]
        raw_data = json.loads(contents)
        raw_data = raw_data["props"]["pageProps"]["listing"]

        data = json.loads(contents)
        data = data["props"]["pageProps"]["listing"]
        data = snake_case_keys(data)

        if data.get("first_registration_date", None):
            first_registration_date = datetime(
                data["first_registration_date"]["year"],
                data["first_registration_date"]["month"],
                1)
            data["first_registration_date"] = first_registration_date

        data["body_type"] = BodyType.get_body_type(data["body_type"]).value
        data["drive_type"] = DriveType.get_drive_type(data["drive_type"]).value
        data["transmission_type"] = TransmissionType.get_transmission_type(data["transmission_type"]).value
        data["fuel_type"] = FuelType.get_fuel_type(data["fuel_type"]).value
        data["variant"] = data["type"].replace(data["make"], "").strip()

        images = list()
        for image in data["images"]:
            images.append("https://images.carforyou.ch/" + image["s3Key"])
        del data["images"]

        return data, raw_data, images

    if url.startswith("https://www.tutti.ch/"):
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        pattern = re.compile("window.__INITIAL_STATE__=.*")

        def is_script(elm: Tag):
            if not elm:
                return False

            if elm.name != "script":
                return False

            match = elm.contents and pattern.search(elm.contents[0])
            if match:
                return True

            return False

        script = soup.find(is_script)
        pattern = re.compile("window.__INITIAL_STATE__=(.*)")
        match = pattern.search(script.contents[0])
        contents = match.group(1)
        raw_data = json.loads(contents)
        raw_data = raw_data["items"][next(iter(raw_data["items"].keys()))]

        data = json.loads(contents)
        data = data["items"][next(iter(data["items"].keys()))]
        data = snake_case_keys(data)

        for obj in data["parameters"]:
            data[obj["id"]] = obj["value"]

        for obj in data["ordered_parameters"]:
            data[obj["id"]] = obj["value"]

        data["make"] = data["brand"]
        data["variant"] = data["subject"].replace(data["make"], "").strip()
        data["transmission_type"] = TransmissionType.get_transmission_type(data["gearbox"]).value
        data["fuel_type"] = FuelType.get_fuel_type(data["fuel"]).value
        data["first_registration_year"] = int(data["regdate"])
        data["horse_power"] = int("".join(s for s in data["hp"] if s.isdigit()))
        data["body_type"] = BodyType.get_body_type(data["car_type"]).value
        data["price"] = int("".join(s for s in data["price"] if s.isdigit()))
        data["mileage"] = int("".join(s for s in next(iter(data["mileage"].split("-"))) if s.isdigit()))

        images = list()
        for image in data["image_names"]:
            images.append("https://c.tutti.ch/images/" + image)
        del data["image_names"]

        return data, raw_data, images


car_input = api.model("CarInput", {
    "url": fields.String(description="A URL to the car listing.", required=True),
    "make_id": fields.Integer(description="The ID to the car make in case aliases should be created or used.", required=False),
})


@api.route("/cars")
class CarsController(Resource):
    def get(self):
        cars_schema = CarSchema(many=True)
        cars = Car.query.all()

        return cars_schema.dump(cars)

    @api.doc(body=car_input)
    def post(self):
        url = api.payload["url"]

        car = Car.query.filter(Car.url == url).first()
        if car:
            abort(400, "This car has already been added to the database.")

        data, raw_data, images = get_car_data(url)

        if "make_id" in api.payload:
            make: Make = Make.query.filter(Make.id == api.payload["make_id"]).first()

            if make.name != data["make"]:
                for alias in make.aliases:
                    if alias.name == data["make"]:
                        break
                else:
                    make_alias = MakeAlias(name=data["make"], make=make)
                    db.session.add(make_alias)
                    db.session.commit()
        else:
            make = Make.query.filter(Make.name == data["make"]).first()

            if not make:
                make_alias: MakeAlias = MakeAlias.query.filter(MakeAlias.name == data["make"]).first()
                if make_alias:
                    make = make_alias.make
                else:
                    make = Make(name=data["make"])
                    db.session.add(make)
                    db.session.commit()

        del data["make"]
        data["make_id"] = make.id

        def default(o):
            if isinstance(o, (date, datetime)):
                return o.isoformat()

        car_schema = CarSchema()

        if "id" in data:
            del data["id"]

        car = Car(
            data=json.dumps(raw_data, default=default),
            url=url,
            **data)

        for image in images:
            img = Image(url=image)
            db.session.add(img)
            db.session.commit()
            car_img = CarImage(image=img, car=car)
            db.session.add(car_img)
            db.session.commit()

        db.session.add(car)
        db.session.commit()

        return car_schema.dump(car)
