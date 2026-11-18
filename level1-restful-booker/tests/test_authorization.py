def test_update_booking_with_token(
    api_client, auth_token, booking_id
):

    api_client.set_token(auth_token)

    updated_data = {
        "firstname": "Updated",
        "lastname": "TokenTest",
        "totalprice": 2500,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-12-10",
            "checkout": "2026-12-15"
        },
        "additionalneeds": "Lunch"
    }

    response = api_client.put(
        f"/booking/{booking_id}",
        json=updated_data
    )

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["firstname"] == "Updated"
    assert response_data["totalprice"] == 2500


def test_update_booking_with_basic_auth(
    api_client, booking_id
):

    api_client.session.cookies.clear()
    
    api_client.set_basic_auth(
        "admin",
        "password123"
    )

    updated_data = {
        "firstname": "Updated",
        "lastname": "BasicAuthTest",
        "totalprice": 3000,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2026-12-20",
            "checkout": "2026-12-25"
        },
        "additionalneeds": "Dinner"
    }

    response = api_client.put(
        f"/booking/{booking_id}",
        json=updated_data
    )

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["firstname"] == "Updated"
    assert response_data["totalprice"] == 3000
