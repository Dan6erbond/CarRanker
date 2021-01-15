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
