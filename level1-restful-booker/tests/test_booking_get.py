def test_get_booking(api_client, booking_id):

    response = api_client.get(
        f"/booking/{booking_id}"
    )

    assert response.status_code == 200

    booking = response.json()

    assert booking["firstname"] == "Kanishkaa"
    assert booking["lastname"] == "Tester"
    assert booking["totalprice"] == 1500
    assert booking["depositpaid"] is True

    assert "bookingdates" in booking


def test_get_nonexistent_booking(api_client):

    response = api_client.get("/booking/999999999")

    assert response.status_code == 404
