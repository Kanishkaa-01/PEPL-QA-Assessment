import pytest


def test_valid_authentication(api_client):

    payload = {
        "username": "admin",
        "password": "password123"
    }

    response = api_client.post(
        "/auth",
        json=payload
    )

    assert response.status_code == 200

    response_data = response.json()

    assert "token" in response_data
    assert response_data["token"] is not None
    assert len(response_data["token"]) > 0


@pytest.mark.parametrize(
    "username, password",
    [
        ("wronguser", "password123"),
        ("admin", "wrongpassword"),
        ("wronguser", "wrongpassword"),
        ("", "password123"),
        ("admin", ""),
    ]
)
def test_invalid_authentication(
    api_client, username, password
):

    payload = {
        "username": username,
        "password": password
    }

    response = api_client.post(
        "/auth",
        json=payload
    )

    assert response.status_code == 200

    response_data = response.json()

    assert "reason" in response_data
    assert response_data["reason"] == "Bad credentials"
