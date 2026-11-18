import os
import pytest

from utils.api_client import APIClient
from utils.test_data import create_booking_data
from pytest_metadata.plugin import metadata_key

@pytest.fixture(scope="function")
def api_client():

    client = APIClient()

    yield client

    client.close()


@pytest.fixture(scope="function")
def auth_token(api_client):

    payload = {
        "username": "admin",
        "password": "password123"
    }

    response = api_client.post(
        "/auth",
        json=payload
    )

    assert response.status_code == 200

    token = response.json()["token"]

    assert token

    return token


@pytest.fixture(scope="function")
def booking_id(api_client, auth_token):

    api_client.set_token(auth_token)

    response = api_client.post(
        "/booking",
        json=create_booking_data()
    )

    assert response.status_code == 200

    booking_id = response.json()["bookingid"]

    yield booking_id

    # Clean up using token authentication
    api_client.set_token(auth_token)
    api_client.delete(f"/booking/{booking_id}")

#HTML Report
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = (
        "Restful Booker API Testing"
    )

    config.stash[metadata_key]["Application URL"] = os.getenv(
        "BASE_URL", "http://localhost:3001"
    )

    config.stash[metadata_key]["Test Framework"] = "Pytest"

    config.stash[metadata_key]["Test Type"] = "API Automation Testing"

    config.stash[metadata_key]["Execution Environment"] = os.getenv(
        "TEST_ENV", "Local"
    )

    config.stash[metadata_key]["Execution Command"] = (
        "pytest -v --html=reports/report.html --self-contained-html"
    )


def pytest_html_report_title(report):
    report.title = "Restful Booker API - Test Execution Report"