import json
import re
from datetime import date, datetime

import requests
from app.database.models.car import BodyType, CarSchema, DriveType, FuelType, TransmissionType
from bs4 import BeautifulSoup, Tag
from flask_restplus import Resource, fields

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

        first_registration_date = datetime(
            data["first_registration_date"]["year"],
            data["first_registration_date"]["month"],
            1)

        data["first_registration_date"] = first_registration_date
        data["body_type"] = BodyType.get_body_type(data["body_type"]).value
        data["drive_type"] = DriveType.get_drive_type(data["drive_type"]).value
        data["transmission_type"] = TransmissionType.get_transmission_type(data["transmission_type"]).value
        data["fuel_type"] = FuelType.get_fuel_type(data["fuel_type"]).value
        data["variant"] = data["type"].replace(data["make"]).strip()

        return data, raw_data

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
        data["variant"] = data["subject"].replace(data["make"]).strip()
        data["transmission_type"] = TransmissionType.get_transmission_type(data["gearbox"]).value
        data["fuel_type"] = FuelType.get_fuel_type(data["fuel"]).value
        data["first_registration_year"] = int(data["regdate"])
        data["horse_power"] = int("".join(s for s in data["hp"] if s.isdigit()))
        data["body_type"] = BodyType.get_body_type(data["car_type"]).value
        data["price"] = int("".join(s for s in data["price"] if s.isdigit()))
        data["mileage"] = int("".join(s for s in next(iter(data["mileage"].split("-"))) if s.isdigit()))

        return data, raw_data

    return None, None

car_input = api.model("CarInput", {
    "url": fields.String(description="A URL to the car listing.", required=True)
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

        data, raw_data = get_car_data(url)

        make = Make.query.filter(Make.name == data["make"]).first()
        if not make:
            make = Make(name=data["make"])
            db.session.add(make)
        make = Make.query.filter(Make.name == data["make"]).first()

        del data["make"]
        data["make_id"] = make.id

        if "images" in data:
            del data["images"]

        def default(o):
            if isinstance(o, (date, datetime)):
                return o.isoformat()

        car_schema = CarSchema()
        car = Car(
            data=json.dumps(raw_data, default=default),
            url=url,
            **data)

        db.session.add(car)
        db.session.commit()

        return car_schema.dump(car)
