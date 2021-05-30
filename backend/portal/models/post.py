import arrow
#from mo.filestorage.sqlalchemy_types import File
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Unicode, Text
from sqlalchemy.orm import backref, relation
from sqlalchemy_utils import ArrowType

from .base import Model


class Post(Model):

    id = Column(Integer, primary_key=True)

    title = Column(String, nullable=False)
    body = Column(Text)
    short_body = Column(Text)
    author = Column(Unicode)
    slug = Column(Unicode, nullable=False, unique=True)
    # logo = Column(File(config_key='storages.UploadedFile'))
    is_player = Column(Boolean, nullable=False, default=False)
    personal_number = Column(Integer)

    date_birthday = Column(ArrowType, nullable=False)
    registered_at = Column(ArrowType, default=arrow.utcnow, nullable=False)

    account_id = Column(ForeignKey('account.id'), nullable=True)
    account = relation('Account', backref=backref('account', uselist=False))

    is_deleted = Column(Boolean, nullable=False, default=False)
