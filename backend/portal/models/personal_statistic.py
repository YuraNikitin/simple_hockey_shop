from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Unicode
from sqlalchemy.orm import backref, relation

from .base import Model


class PersonalStatistic(Model):
    id = Column(Integer, primary_key=True)

    games = Column(Integer)
    goals = Column(Integer)
    scores = Column(Integer)
    penalty_min = Column(Integer)

    account_id = Column(ForeignKey('account.id'), nullable=False)
    account = relation('Account', backref=backref('account', uselist=False))
