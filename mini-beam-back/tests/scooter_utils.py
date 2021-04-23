import math
import random
import uuid
from typing import Dict, List, Tuple

import geog
import numpy as np
from shapely.geometry import Point, Polygon
from sqlalchemy.orm import Session

from models.location import Location
from models.scooter import Scooter
from schemas.scooters import ScooterLocationResponse


def create_poly(lat: float, lng: float, distance: float = 100.0) -> Polygon:
    p = Point([lng, lat])
    n_points = 20
    angles = np.linspace(0, 360, n_points)
    polygon = geog.propagate(p, angles, distance)
    poly = Polygon(polygon)
    return poly


def random_points_within(poly: Polygon) -> Point:
    min_x, min_y, max_x, max_y = poly.bounds

    while True:
        random_point = Point(
            [random.uniform(min_x, max_x), random.uniform(min_y, max_y)]
        )
        if random_point.within(poly):
            return random_point


def get_endpoints_at_distance(
    lat1: float,
    lon1: float,
    d: float,
    bearing: float = 317.662819,
) -> Tuple[float, float]:
    # Radius of the Earth
    R = 6378.1
    # convert degrees to radians
    brng = math.radians(bearing)
    # convert nautical miles to km
    d = d * 1.852
    lat2 = math.asin(
        math.sin(lat1) * math.cos(d / R)
        + math.cos(lat1) * math.sin(d / R) * math.cos(brng)
    )
    lon2 = lon1 + math.atan2(
        math.sin(brng) * math.sin(d / R) * math.cos(lat1),
        math.cos(d / R) - math.sin(lat1) * math.sin(lat2),
    )
    return lat2, lon2


def assert_slc_list(data_list: List[Dict], search_distance: float):
    before_distance = 0
    for data in data_list:
        new_slc = ScooterLocationResponse(**data)
        assert new_slc.distance >= before_distance
        assert new_slc.distance <= search_distance
        before_distance = new_slc.distance


class ScooterLocationCreator(object):
    def __init__(
        self,
        session: Session,
        lat: float = 1.32874127,
        lng: float = 103.842717,
        distance: float = 100,
    ):
        self.session = session
        self.lat = lat
        self.lng = lng
        self.distance = distance
        self.poly = create_poly(lat, lng, distance)

    def create_location(self, scooter: Scooter, **kwargs) -> Location:
        point = random_points_within(self.poly)
        # Random point located in Singapore
        default = {
            "parked": True,
            "scooterId": scooter.serialNo,
            "lat": point.y,
            "lng": point.x,
        }
        default.update(kwargs)
        location = Location(**default)
        self.session.add(location)
        self.session.commit()
        return scooter

    def create_scooter(self, **kwargs) -> Scooter:
        default = {
            "serialNo": str(uuid.uuid4()),
            "modelNo": str(uuid.uuid4()),
        }
        default.update(kwargs)
        scooter = Scooter(**default)
        self.session.add(scooter)
        self.session.commit()
        return scooter

    def create_scooter_location(
        self,
        scooter_dict: Dict = {},
        location_dict: Dict = {},
    ) -> Tuple[Scooter, Location]:
        scooter = self.create_scooter(**scooter_dict)
        location = self.create_location(scooter, **location_dict)
        return scooter, location
