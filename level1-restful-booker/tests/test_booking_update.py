def test_update_booking(api_client, auth_token, booking_id):

    api_client.set_token(auth_token)

    updated_data = {
        "firstname": "Updated",
        "lastname": "Booking",
        "totalprice": 3000,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2026-12-10",
            "checkout": "2026-12-20"
        },
        "additionalneeds": "Dinner"
    }

    response = api_client.put(
        f"/booking/{booking_id}",
        json=updated_data
    )

    assert response.status_code == 200

    updated_booking = response.json()

    assert updated_booking["firstname"] == "Updated"
    assert updated_booking["lastname"] == "Booking"
    assert updated_booking["totalprice"] == 3000
    assert updated_booking["depositpaid"] is False

    # Verify the changes using GET
    get_response = api_client.get(
        f"/booking/{booking_id}"
    )

    assert get_response.status_code == 200

    assert get_response.json()["firstname"] == "Updated"


def test_patch_booking(api_client, auth_token, booking_id):

    api_client.set_token(auth_token)

    patch_data = {
        "firstname": "Patched"
    }

    response = api_client.patch(
        f"/booking/{booking_id}",
        json=patch_data
    )

    assert response.status_code == 200

    patched_booking = response.json()

    assert patched_booking["firstname"] == "Patched"

    # Verify unchanged fields
    assert patched_booking["lastname"] == "Tester"
    assert patched_booking["totalprice"] == 1500
