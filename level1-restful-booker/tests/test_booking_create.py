def test_create_booking(api_client, auth_token):

    api_client.set_token(auth_token)

    booking_data = {
        "firstname": "Create",
        "lastname": "Test",
        "totalprice": 2000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-12-10",
            "checkout": "2026-12-15"
        },
        "additionalneeds": "Breakfast"
    }

    response = api_client.post(
        "/booking",
        json=booking_data
    )

    assert response.status_code == 200

    response_data = response.json()

    assert "bookingid" in response_data
    assert response_data["bookingid"] is not None

    assert "booking" in response_data

    created_booking = response_data["booking"]

    assert created_booking["firstname"] == "Create"
    assert created_booking["lastname"] == "Test"
    assert created_booking["totalprice"] == 2000
    assert created_booking["depositpaid"] is True

    # Verify booking dates
    assert created_booking["bookingdates"]["checkin"] == "2026-12-10"
    assert created_booking["bookingdates"]["checkout"] == "2026-12-15"

    # Clean up the created booking
    api_client.delete(
        f"/booking/{response_data['bookingid']}"
    )
