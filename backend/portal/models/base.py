from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import scoped_session, sessionmaker

from portal import helpers as h


class Model:

    @declared_attr
    def __tablename__(cls):
        return h.uncamelcase(cls.__name__)


Model = declarative_base(cls=Model)


def session_factory(sa_dsn):
    engine = create_engine(sa_dsn)
    Model.metadata.bind = engine
    return scoped_session(sessionmaker(bind=engine))
