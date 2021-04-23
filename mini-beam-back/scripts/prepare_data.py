import argparse

from sqlalchemy.orm import Session

from db.session import SessionLocal, SessionTest
from tests.scooter_utils import ScooterLocationCreator


def create_scooter(
    session: Session,
    lat: float = 1.358817,
    lng: float = 103.872186,
    target_distance: float = 10000.0,
    location_count: int = 1000,
):
    target_distance = 10000
    slc = ScooterLocationCreator(
        session=session, lat=lat, lng=lng, distance=target_distance
    )
    for _ in range(location_count):
        slc.create_scooter_location()


def init():
    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("-t", action="store_true")
        parser.add_argument("-c", nargs="?", const=1000, type=int, default=1000)
        args = parser.parse_args()
        is_test = args.t
        counts = args.c
        session_map = {
            True: SessionTest,
            False: SessionLocal,
        }
        with session_map[is_test]() as session:
            create_scooter(session=session, location_count=counts)


init()
