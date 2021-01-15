from flask import Blueprint
from flask_restplus import Api

blueprint = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(blueprint, version='1.0', title='CarRanker',
          description='A webscraper API for cars from various listing sites, with ranking functionality and data aggregation.')
