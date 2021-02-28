from .base import Base
from ..db import db


class Image(Base):

    __tablename__ = "images"

    url = db.Column(db.String(256), nullable=False)
