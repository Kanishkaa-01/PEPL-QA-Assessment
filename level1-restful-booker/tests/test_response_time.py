
def test_ping_response_time(api_client):

    response = api_client.get("/ping")

    assert response.status_code == 201

    response_time = response.elapsed.total_seconds()

    assert response_time < 2.0, (
        f"API response took {response_time:.3f} seconds"
    )
