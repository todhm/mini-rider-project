from sqlalchemy import Column, DateTime, String

from db.base_class import Base
from utils.time_utils import get_now_time


class Scooter(Base):
    __tablename__ = "scooter"
    serialNo = Column(String, primary_key=True)
    modelNo = Column(String)
    createdDate = Column(DateTime, default=get_now_time)
    modifyDate = Column(DateTime, onupdate=get_now_time)
