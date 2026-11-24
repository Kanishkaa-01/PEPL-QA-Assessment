
import os
import pytest


@pytest.fixture(scope="session")
def base_url():
    """
    Returns the website URL.
    Uses the reference website by default.
    Can be changed using the BASE_URL environment variable.
    """
    return os.getenv(
        "BASE_URL",
        "https://practicesoftwaretesting.com"
    )
