from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import backref, relation

from .base import Model


class Standings(Model):

    id = Column(Integer, primary_key=True)

    position = Column(Integer)
    games = Column(Integer)
    win_games = Column(Integer)
    loose_games = Column(Integer)
    scores = Column(Integer)
    win_on_shootouts = Column(Integer)
    loose_on_shootouts = Column(Integer)

    team_id = Column(ForeignKey('team.id'), nullable=False)
    team = relation('Team', backref=backref('team', uselist=False))
