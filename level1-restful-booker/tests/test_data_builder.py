
from utils.test_data import create_booking_data


def test_booking_data_builder():

    booking = create_booking_data()

    assert booking["firstname"] == "Kanishkaa"
    assert booking["lastname"] == "Tester"
    assert booking["totalprice"] == 1500
    assert booking["depositpaid"] is True

    assert "checkin" in booking["bookingdates"]
    assert "checkout" in booking["bookingdates"]


def test_booking_data_overrides():

    booking = create_booking_data(
        firstname="Rahul",
        totalprice=2500
    )

    assert booking["firstname"] == "Rahul"
    assert booking["totalprice"] == 2500
