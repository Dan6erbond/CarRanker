import json
import sqlite3

import flask
import requests
from bs4 import BeautifulSoup
from flask import jsonify, request, g


DATABASE = "./tmp/data.db"


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def get_car_data(url):
    if url.startswith("https://www.carforyou.ch"):
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        data = soup.find(id="__NEXT_DATA__")
        data = json.loads(data.contents[0])
        return data["props"]["pageProps"]["listing"]


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/v1/cars', methods=["GET", "POST"])
def scrape_car():
    if request.method == "POST":
        url = request.form.get("url") or request.data.get("url")
    else:
        url = "https://www.carforyou.ch/en/auto/saloon/vw/passat/20-bluetdi-comfortline-dsg-214965"
    return jsonify(get_car_data(url))


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == "__main__":
    app.run()
