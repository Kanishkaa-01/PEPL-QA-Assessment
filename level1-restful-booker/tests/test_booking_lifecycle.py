from utils.test_data import create_booking_data


def test_complete_booking_lifecycle(api_client, auth_token):

    api_client.set_token(auth_token)

    # 1. CREATE
    booking_data = create_booking_data()

    create_response = api_client.post(
        "/booking",
        json=booking_data
    )

    assert create_response.status_code == 200

    booking_id = create_response.json()["bookingid"]

    assert booking_id is not None

    # 2. READ
    read_response = api_client.get(
        f"/booking/{booking_id}"
    )

    assert read_response.status_code == 200

    assert read_response.json()["firstname"] == booking_data["firstname"]

    # 3. UPDATE - PUT
    updated_data = create_booking_data(
        firstname="LifecycleUpdated",
        totalprice=3000
    )

    update_response = api_client.put(
        f"/booking/{booking_id}",
        json=updated_data
    )

    assert update_response.status_code == 200

    assert update_response.json()["firstname"] == "LifecycleUpdated"

    # 4. PARTIAL UPDATE - PATCH
    patch_response = api_client.patch(
        f"/booking/{booking_id}",
        json={"firstname": "LifecyclePatched"}
    )

    assert patch_response.status_code == 200

    assert patch_response.json()["firstname"] == "LifecyclePatched"

    # 5. DELETE
    delete_response = api_client.delete(
        f"/booking/{booking_id}"
    )

    assert delete_response.status_code == 201

    # 6. CONFIRM DELETION
    final_response = api_client.get(
        f"/booking/{booking_id}"
    )

    assert final_response.status_code == 404
