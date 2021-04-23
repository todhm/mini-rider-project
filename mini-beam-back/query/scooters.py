from typing import List, Optional

from geoalchemy2 import Geography, func
from sqlalchemy import cast
from sqlalchemy.orm import Session

from models.location import Location
from models.scooter import Scooter
from schemas.scooters import ScooterLocationResponse


def find_scooter_within(
    session: Session,
    lat: float,
    lng: float,
    distance_meter: float,
    limit: Optional[int] = None,
) -> List[ScooterLocationResponse]:
    point = f"SRID=4326;POINT({lng} {lat})"
    distance_query = Location.coordinates.ST_Distance_Sphere(point).label("distance")
    base_query = (
        session.query(
            Scooter,
            func.st_y(Location.coordinates),
            func.st_x(Location.coordinates),
            Location,
            distance_query,
        )
        .filter(
            func.ST_DWithin(
                cast(Location.coordinates, Geography),
                cast(point, Geography),
                distance_meter,
            )
        )
        .filter(Location.scooterId == Scooter.serialNo)
        .order_by("distance")
    )
    if limit:
        base_query = base_query.limit(limit)
    return_list = []
    data_list = base_query.all()
    for scooter, lat, lng, location, distance in data_list:
        return_list.append(
            ScooterLocationResponse(
                serialNo=scooter.serialNo,
                modelNo=scooter.modelNo,
                parked=location.parked,
                lat=lat,
                lng=lng,
                distance=distance,
            )
        )
    return return_list
