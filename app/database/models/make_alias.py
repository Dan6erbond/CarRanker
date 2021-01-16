from typing import TYPE_CHECKING

from ..db import db
from .base import Base

if TYPE_CHECKING:
    from .make import Make


class MakeAlias(Base):

    __tablename__ = "make_aliases"

    make_id = db.Column(db.Integer, db.ForeignKey("makes.id"), nullable=False)
    make: "Make" = db.relationship("Make")
    name = db.Column(db.String(64), nullable=False)
