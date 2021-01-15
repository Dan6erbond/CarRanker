import json

import requests
from bs4 import BeautifulSoup
from flask import current_app as app
from flask import request

from ....database.models import Car, CarSchema
from ....helpers import snake_case_keys


def get_car_data(url):
    if url.startswith("https://www.carforyou.ch"):
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        data = soup.find(id="__NEXT_DATA__")
        data = json.loads(data.contents[0])
        return data["props"]["pageProps"]["listing"]


@app.route('/api/v1/cars', methods=["GET", "POST"])
def scrape_car():
    if request.method == "POST":
        url = request.form.get("url") or request.data.get("url")
    else:
        url = "https://www.carforyou.ch/en/auto/saloon/vw/passat/20-bluetdi-comfortline-dsg-214965"

    car = get_car_data(url)
    car = snake_case_keys(car)
    car = Car(data=car, **car)

    car_schema = CarSchema()

    return car_schema.dump(car)
