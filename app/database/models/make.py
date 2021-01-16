from .base import Base
from ..db import db


class Make(Base):

    __tablename__ = "makes"

    name = db.Column(db.String(64), nullable=False)
    cars = db.relationship("Car")
    aliases = db.relationship("MakeAlias")
