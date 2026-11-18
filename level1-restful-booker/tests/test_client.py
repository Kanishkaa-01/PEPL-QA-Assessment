from utils.api_client import APIClient


def test_api_client_ping():

    client = APIClient()

    response = client.get("/ping")

    assert response.status_code == 201
    assert response.text == "Created"

    client.close()
