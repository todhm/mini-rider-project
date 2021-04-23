from typing import Optional

from pydantic import BaseModel


class ScooterSearchSchema(BaseModel):
    lat: float
    lng: float
    searchRadius: float = 100.0
    numScooters: Optional[int] = None


class ScooterLocationResponse(BaseModel):

    serialNo: str
    modelNo: str
    parked: bool
    lat: float
    lng: float
    distance: float
