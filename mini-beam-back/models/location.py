from geoalchemy2 import Geometry
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String

from db.base_class import Base
from utils.time_utils import get_now_time


class Location(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True, autoincrement=True)
    parked = Column(Boolean, default=True)
    coordinates = Column(Geometry("POINT"))
    scooterId = Column(String, ForeignKey("scooter.serialNo", on_delete="SET NULL"))
    createdDate = Column(DateTime, default=get_now_time)
    modifyDate = Column(DateTime, onupdate=get_now_time)

    def __init__(self, lat: float, lng: float, scooterId: str, parked: bool = True):
        self.coordinates = f"SRID=4326;POINT({lng} {lat})"
        self.scooterId = scooterId
        self.parked = parked
