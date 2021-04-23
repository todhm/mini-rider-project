import geog
import numpy as np
from shapely.geometry import Point, Polygon


def create_poly(lat: float, lng: float, distance: float = 100.0) -> Polygon:
    p = Point([lng, lat])
    n_points = 20
    distance = 10 * distance
    angles = np.linspace(0, 360, n_points)
    polygon = geog.propagate(p, angles, distance)
    return polygon
