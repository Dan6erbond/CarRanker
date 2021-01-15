from .base import Base
from ..db import db


class CarScore(Base):

    __tablename__ = "car_scores"

    car_id = db.Column(db.Integer, db.ForeignKey("cars.id"), nullable=False)
    car = db.relationship("Car")

    car_score_weight_id = db.Column(db.Integer, db.ForeignKey("car_score_weights.id"), nullable=False)
    car_score_weight = db.relationship("CarScoreWeight")

    interior_score = db.Column(db.Integer, nullable=False)
    exterior_score = db.Column(db.Integer, nullable=False)
    equipment_score = db.Column(db.Integer, nullable=False)
    design_score = db.Column(db.Integer, nullable=False)
    run_costs_score = db.Column(db.Integer, nullable=False)
    maintenance_score = db.Column(db.Integer, nullable=False)
