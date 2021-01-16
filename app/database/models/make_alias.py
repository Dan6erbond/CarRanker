from .base import Base
from ..db import db


class MakeAlias(Base):

    __tablename__ = "make_aliases"

    make_id = db.Column(db.Integer, db.ForeignKey("makes.id"), nullable=False)
    make = db.relationship("Make")
    name = db.Column(db.String(64), nullable=False)
