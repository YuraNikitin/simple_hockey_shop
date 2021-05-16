import arrow
from sqlalchemy import Column, Integer, String, Unicode
from sqlalchemy_utils import ArrowType

from .base import Model


class Account(Model):

    id = Column(Integer, primary_key=True)
    email = Column(Unicode, unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)

    registered_at = Column(ArrowType, default=arrow.utcnow, nullable=False)
