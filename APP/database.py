from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import APP.models

engine = create_engine('mysql+pymysql://root:root@localhost:3306/farmfood?charset=utf8', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwixse
    # you will have to import them first before calling init_db()

    Base.metadata.create_all(bind=engine)
