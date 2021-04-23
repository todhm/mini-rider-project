import argparse
from unittest import mock

from sqlalchemy import func

from db.session import SessionTest
from models.scooter import Scooter


def test_creation_script(test_app):
    test_count = 10
    from scripts import prepare_data

    with mock.patch.object(prepare_data, "__name__", "__main__"):
        with mock.patch(
            "scripts.prepare_data.argparse.ArgumentParser.parse_args",
            return_value=argparse.Namespace(t=True, c=test_count),
        ):
            prepare_data.init()

    with SessionTest() as session:
        scooter_count = session.query(func.count(Scooter.serialNo)).scalar()
    assert scooter_count == test_count
