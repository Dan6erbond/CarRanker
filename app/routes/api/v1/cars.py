import json

import requests
from bs4 import BeautifulSoup
from flask import request
from flask_restplus import Resource, reqparse

from ....database.db import db
from ....database.models import Car, CarSchema
from ....helpers import snake_case_keys
from .api import api


def get_car_data(url):
    if url.startswith("https://www.carforyou.ch"):
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        data = soup.find(id="__NEXT_DATA__")
        data = json.loads(data.contents[0])
        return data["props"]["pageProps"]["listing"]


car_fields = api.model("Car", {
    "id": fields.Integer,
    "url": fields.String,
    "model": fields.String,
    "variant": fields.String,
    "type_full": fields.String,
    "price": fields.Integer,
    "horse_power": fields.Integer,
    "cylinders": fields.Integer,
    "first_registration_year": fields.Integer,
    "first_registration_date": fields.Date,
    "transmission_type": fields.String,
    "fuel_type": fields.String,
    "body_type": fields.String,
    "seats": fields.Integer,
    "doors": fields.Integer,
    "drive_type": fields.String,
    "mileage": fields.Integer,
    "consumption_combined": fields.Integer,
})


@api.route("/cars")
class CarsController(Resource):
    def get(self):
        cars_schema = CarSchema(many=True)

        cars = Car.query.all()
        items = cars_schema.dump(cars)

        return {"cars": items}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('rate', type=int, help='Rate to charge for this resource')
        args = parser.parse_args()

        url = request.form.get("url") or request.data.get("url")

        car = get_car_data(url)
        car = snake_case_keys(car)
        car = Car(data=car, url=url, variant=car["type"], **car)

        db.session.add(car)
        db.session.commit()

        car_schema = CarSchema()

        return car_schema.dump(car)
