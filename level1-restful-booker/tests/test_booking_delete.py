def test_delete_booking(api_client, auth_token):

    api_client.set_token(auth_token)

    booking_data = {
        "firstname": "Delete",
        "lastname": "Test",
        "totalprice": 1000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-12-10",
            "checkout": "2026-12-15"
        },
        "additionalneeds": "None"
    }

    create_response = api_client.post(
        "/booking",
        json=booking_data
    )

    assert create_response.status_code == 200

    booking_id = create_response.json()["bookingid"]

    delete_response = api_client.delete(
        f"/booking/{booking_id}"
    )

    assert delete_response.status_code == 201

    # Confirm the booking no longer exists
    get_response = api_client.get(
        f"/booking/{booking_id}"
    )

    assert get_response.status_code == 404
