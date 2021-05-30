import arrow
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Unicode
from sqlalchemy.orm import backref, relation
from sqlalchemy_utils import ArrowType

from .base import Model


class Account(Model):

    id = Column(Integer, primary_key=True)
    login = Column(Unicode, unique=True, nullable=False)
    email = Column(Unicode, unique=True, nullable=False)
    password = Column(String, nullable=False)

    name = Column(String, nullable=False)
    is_player = Column(Boolean, nullable=False, default=False)
    personal_number = Column(Integer)

    date_birthday = Column(ArrowType, nullable=False)
    registered_at = Column(ArrowType, default=arrow.utcnow, nullable=False)

    position_id = Column(ForeignKey('position.id'), nullable=True)
    position = relation('Position', backref=backref('position', uselist=False))

    is_deleted = Column(Boolean, nullable=False, default=False)
