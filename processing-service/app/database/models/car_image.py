from .base import Base
from ..db import db


class CarImage(Base):

    __tablename__ = "cars_images"

    car_id = db.Column(db.Integer, db.ForeignKey("cars.id"), nullable=False)
    car = db.relationship("Car")
    image_id = db.Column(db.Integer, db.ForeignKey("images.id"), nullable=False)
    image = db.relationship("Image")
