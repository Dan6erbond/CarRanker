from .base import Base
from ..db import db


class CarScoreWeight(Base):

    __tablename__ = "car_score_weights"

    interior_score = db.Column(db.Integer, nullable=False)
    exterior_score = db.Column(db.Integer, nullable=False)
    equipment_score = db.Column(db.Integer, nullable=False)
    design_score = db.Column(db.Integer, nullable=False)
    run_costs_score = db.Column(db.Integer, nullable=False)
    maintenance_score = db.Column(db.Integer, nullable=False)

    scores = db.relationship("CarScore")
