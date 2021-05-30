import arrow
#from mo.filestorage.sqlalchemy_types import File
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Unicode
from sqlalchemy.orm import backref, relation
from sqlalchemy_utils import ArrowType

from .base import Model


class Team(Model):
    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)
    registered_at = Column(ArrowType, default=arrow.utcnow, nullable=False)
    #logo = Column(File(config_key='storages.UploadedFile'))

    group_id = Column(ForeignKey('group.id'), nullable=False)
    group = relation('Group', backref=backref('group', uselist=False))

    is_deleted = Column(Boolean, nullable=False, default=False)
