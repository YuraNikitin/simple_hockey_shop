from sqlalchemy import Column, Integer, String

from .base import Model


class Group(Model):

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
