import json
from datetime import date, datetime

import requests
from app.database.models.car import BodyType, CarSchema, DriveType
from bs4 import BeautifulSoup
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

        data = soup.find(id="__NEXT_DATA__")
        contents = data.contents[0]
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

        return data, raw_data



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

        del data["images"]

        def default(o):
            if isinstance(o, (date, datetime)):
                return o.isoformat()

        car_schema = CarSchema()
        car = Car(
            data=json.dumps(raw_data, default=default),
            url=url, variant=data["type"],
            **data)

        db.session.add(car)
        db.session.commit()

        return car_schema.dump(car)
