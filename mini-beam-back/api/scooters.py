import logging
import traceback
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.session import get_session
from query.scooters import find_scooter_within
from schemas.scooters import ScooterLocationResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
scooterapp = APIRouter()


@scooterapp.get("/scooters", response_model=List[ScooterLocationResponse])
async def scooters(
    lat: float,
    lng: float,
    searchRadius: float = 100.0,
    numScooters: Optional[int] = None,
    session: Session = Depends(get_session),
):
    try:
        return find_scooter_within(
            session, lat=lat, lng=lng, distance_meter=searchRadius, limit=numScooters
        )
    except Exception:
        logger.error("Location query error " + traceback.format_exc())
        raise HTTPException(status_code=400, detail="Location query error")
