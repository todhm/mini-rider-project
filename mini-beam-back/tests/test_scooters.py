from unittest import mock

from sqlalchemy import func

from db.session import SessionTest
from models.scooter import Scooter
from tests.scooter_utils import (
    ScooterLocationCreator,
    assert_slc_list,
    get_endpoints_at_distance,
)


def test_able_to_fetch_scooter_within_locs(test_app):
    lat = 1.32874127
    lng = 103.842717
    search_distance = 100

    newlat, newlng = get_endpoints_at_distance(lat, lng, d=search_distance - 1)

    with SessionTest() as session:
        slc = ScooterLocationCreator(
            session=session, lat=lat, lng=lng, distance=search_distance
        )
        scooter, location = slc.create_scooter_location(
            location_dict={"lat": newlat, "lng": newlng}
        )
    response = test_app.get(
        "/scooters", params={"lat": lat, "lng": lng, "searchRadius": search_distance}
    )
    data_list = response.json()
    assert response.status_code == 200
    data_list = response.json()
    assert len(data_list) == 0
    assert_slc_list(data_list, search_distance)


def test_notfetch_scooter_outside_scope(test_app):
    lat = 1.32874127
    lng = 103.842717
    search_distance = 100

    newlat, newlng = get_endpoints_at_distance(lat, lng, d=search_distance + 100)

    with SessionTest() as session:
        slc = ScooterLocationCreator(session=session)
        scooter, location = slc.create_scooter_location(
            location_dict={"lng": newlng, "lat": newlat}
        )
    response = test_app.get(
        "/scooters", params={"lat": lat, "lng": lng, "searchRadius": search_distance}
    )
    data_list = response.json()
    assert response.status_code == 200
    data_list = response.json()
    assert len(data_list) == 0


def test_scooter_search_many_scooters(test_app):
    within_search_num = 10
    out_of_scope_num = 10
    singapore_lat = 1.32874127
    singapore_lng = 103.842717
    korean_lat = 37.56667126
    korean_lng = 126.97806
    distance = 1000
    with SessionTest() as session:
        within_slc = ScooterLocationCreator(
            session=session, lat=singapore_lat, lng=singapore_lng, distance=distance
        )
        for i in range(within_search_num):
            within_slc.create_scooter_location()

        out_of_scope_slc = ScooterLocationCreator(
            session=session, lat=korean_lat, lng=korean_lng, distance=distance
        )
        for i in range(out_of_scope_num):
            out_of_scope_slc.create_scooter_location()
        scooter_count = session.query(func.count(Scooter.serialNo)).scalar()

    assert scooter_count == within_search_num + out_of_scope_num
    response = test_app.get(
        "/scooters",
        params={
            "lat": singapore_lat,
            "lng": singapore_lng,
            "searchRadius": distance,
        },
    )
    data_list = response.json()
    assert response.status_code == 200
    data_list = response.json()
    assert len(data_list) == within_search_num
    assert_slc_list(data_list, distance)

    limit_counts = within_search_num - 5
    response = test_app.get(
        "/scooters",
        params={
            "lat": singapore_lat,
            "lng": singapore_lng,
            "searchRadius": distance,
            "numScooters": limit_counts,
        },
    )
    data_list = response.json()
    assert response.status_code == 200
    data_list = response.json()
    assert len(data_list) == limit_counts
    assert_slc_list(data_list, distance)


def test_fetch_error_case(test_app):
    response = test_app.get("/scooters", params={})
    assert response.status_code == 422
    with mock.patch(
        "api.scooters.find_scooter_within",
    ) as scooterapi:
        scooterapi.side_effect = ValueError("Side Effect")
        lat = 1.32874127
        lng = 103.842717
        search_distance = 100
        response = test_app.get(
            "/scooters",
            params={
                "lat": lat,
                "lng": lng,
                "searchRadius": search_distance,
            },
        )
        assert response.status_code == 400
