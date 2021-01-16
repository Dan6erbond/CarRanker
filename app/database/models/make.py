from typing import TYPE_CHECKING, List

from ..db import db
from .base import Base

if TYPE_CHECKING:
    from .make_alias import MakeAlias


class Make(Base):

    __tablename__ = "makes"

    name = db.Column(db.String(64), nullable=False)
    cars = db.relationship("Car")
    aliases: List["MakeAlias"] = db.relationship("MakeAlias")
