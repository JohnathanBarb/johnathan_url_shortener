from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from johnathan_url_shortener.config import get_settings


def get_dbsession():
    # TODO: dont think engine should be here, think better latter

    engine = create_engine(get_settings().db_url, echo=True)

    return sessionmaker(bind=engine)
