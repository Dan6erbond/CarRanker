import enum

from ..db import db
from ...exts.ma import ma

from .base import Base


class TransmissionType(enum.Enum):
    automatic = "automatic"
    automatic_cvt = "automatic_cvt"
    manual = "manual"


class FuelType(enum.Enum):
    gasoline = "gasoline"
    diesel = "diesel"


class BodyType(enum.Enum):
    sedan = "sedan"
    suv = "suv"
    minivan = "minivan"
    pickup = "pickup"
    hatchback = "hatchback"
    coupe = "coupe"
    station_wagon = "station_wagon"
    convertible = "convertible"


class DriveType(enum.Enum):
    awd = "awd"
    fwd = "fwd"
    rwd = "rwd"


class Car(Base):

    __tablename__ = "cars"

    url = db.Column(db.String(256), nullable=False)

    make_id = db.Column(db.Integer, db.ForeignKey("makes.id"), nullable=False)
    make = db.relationship("Make")
    model = db.Column(db.String(64), nullable=False)
    variant = db.Column(db.String(64), nullable=False)
    type_full = db.Column(db.String(256), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    horse_power = db.Column(db.Integer, nullable=False)
    cylinders = db.Column(db.Integer, nullable=False)
    first_registration_year = db.Column(db.Integer, nullable=False)
    registration_date = db.Column(db.Date, nullable=False)
    transmission_type = db.Column(db.Enum(TransmissionType), nullable=False)
    fuel_type = db.Column(db.Enum(FuelType), nullable=False)
    body_type = db.Column(db.Enum(BodyType), nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    doors = db.Column(db.Integer, nullable=False)
    drive_type = db.Column(db.Enum(DriveType), nullable=False)
    mileage = db.Column(db.Integer, nullable=False)
    consumption_combined = db.Column(db.Float, nullable=False)

    images = db.relationship("Image", secondary="cars_images", backref="Car")

    exterior_front_image_id = db.Column(db.Integer, db.ForeignKey("images.id"), nullable=True)
    exterior_front_image = db.relationship("Image", foreign_keys=[exterior_front_image_id])
    exterior_side_image_id = db.Column(db.Integer, db.ForeignKey("images.id"), nullable=True)
    exterior_side_image = db.relationship("Image", foreign_keys=[exterior_side_image_id])
    exterior_back_image_id = db.Column(db.Integer, db.ForeignKey("images.id"), nullable=True)
    exterior_back_image = db.relationship("Image", foreign_keys=[exterior_back_image_id])
    interior_front_image_id = db.Column(db.Integer, db.ForeignKey("images.id"), nullable=True)
    interior_front_image = db.relationship("Image", foreign_keys=[interior_front_image_id])
    interior_dash_image_id = db.Column(db.Integer, db.ForeignKey("images.id"), nullable=True)
    interior_dash_image = db.relationship("Image", foreign_keys=[interior_dash_image_id])
    interior_back_image_id = db.Column(db.Integer, db.ForeignKey("images.id"), nullable=True)
    interior_back_image = db.relationship("Image", foreign_keys=[interior_back_image_id])
    interior_trunk_image_id = db.Column(db.Integer, db.ForeignKey("images.id"), nullable=True)
    interior_trunk_image = db.relationship("Image", foreign_keys=[interior_trunk_image_id])

    scores = db.relationship("CarScore")

    data = db.Column(db.Text, nullable=False)

    def __init__(self, **entries):
        self.__dict__.update(entries)

class CarSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Car

    id = ma.auto_field()
    url = ma.auto_field()
    model = ma.auto_field()
    variant = ma.auto_field()
    type_full = ma.auto_field()
    price = ma.auto_field()

    horse_power = ma.auto_field()
    cylinders = ma.auto_field()
    first_registration_year = ma.auto_field()
    registration_date = ma.auto_field()
    transmission_type = ma.auto_field()
    fuel_type = ma.auto_field()
    body_type = ma.auto_field()
    seats = ma.auto_field()
    doors = ma.auto_field()
    drive_type = ma.auto_field()
    mileage = ma.auto_field()
    consumption_combined = ma.auto_field()

    data = ma.Dict()
