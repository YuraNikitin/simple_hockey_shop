import arrow
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import backref, relation
from sqlalchemy_utils import ArrowType

from .base import Model


class CalendarGame(Model):

    id = Column(Integer, primary_key=True)

    date_game = Column(ArrowType, default=arrow.utcnow, nullable=False)

    group_id = Column(ForeignKey('group.id'), nullable=False)
    group = relation('Group', backref=backref('group', uselist=False))

    home_team_id = Column(ForeignKey('team.id'), nullable=False)
    guest_team_id = Column(ForeignKey('team.id'), nullable=False)

    home_team = relation('Team', remote_side=[home_team_id])
    guest_team = relation('Team', remote_side=[guest_team_id])
