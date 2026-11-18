
import pytest


@pytest.mark.parametrize(
    "booking_id",
    [
        999999999,
        "invalid",
        -1
    ]
)
def test_get_invalid_booking_id(api_client, booking_id):

    response = api_client.get(
        f"/booking/{booking_id}"
    )

    assert response.status_code == 404


def test_get_booking_with_invalid_format(api_client):

    response = api_client.get("/booking/invalid-id")

    assert response.status_code == 404
