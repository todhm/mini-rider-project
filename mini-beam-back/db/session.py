from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import settings, test_settings

engine = create_engine(settings.DB_URL, pool_pre_ping=True)
test_engine = create_engine(test_settings.DB_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SessionTest = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


def get_session() -> sessionmaker:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_test_session() -> sessionmaker:
    try:
        db = SessionTest()
        yield db
    finally:
        db.close()
