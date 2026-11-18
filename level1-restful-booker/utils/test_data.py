
from datetime import date, timedelta


def create_booking_data(**overrides):
    """
    Generate reusable booking test data.
    """

    checkin = date.today() + timedelta(days=30)
    checkout = checkin + timedelta(days=5)

    booking = {
        "firstname": "Kanishkaa",
        "lastname": "Tester",
        "totalprice": 1500,
        "depositpaid": True,
        "bookingdates": {
            "checkin": checkin.isoformat(),
            "checkout": checkout.isoformat()
        },
        "additionalneeds": "Breakfast"
    }

    booking.update(overrides)

    return booking
