
import os
import requests


class APIClient:

    def __init__(self, base_url=None):
        """
        Initialize the API client.
        """

        self.base_url = (
            base_url
            or os.getenv(
                "BASE_URL",
                "http://localhost:3001"
            )
        ).rstrip("/")

        self.session = requests.Session()

        self.timeout = 10

    def get(self, endpoint, **kwargs):
        """Send a GET request."""

        return self.session.get(
            f"{self.base_url}{endpoint}",
            timeout=self.timeout,
            **kwargs
        )

    def post(self, endpoint, **kwargs):
        """Send a POST request."""

        return self.session.post(
            f"{self.base_url}{endpoint}",
            timeout=self.timeout,
            **kwargs
        )

    def put(self, endpoint, **kwargs):
        """Send a PUT request."""

        return self.session.put(
            f"{self.base_url}{endpoint}",
            timeout=self.timeout,
            **kwargs
        )

    def patch(self, endpoint, **kwargs):
        """Send a PATCH request."""

        return self.session.patch(
            f"{self.base_url}{endpoint}",
            timeout=self.timeout,
            **kwargs
        )

    def delete(self, endpoint, **kwargs):
        """Send a DELETE request."""

        return self.session.delete(
            f"{self.base_url}{endpoint}",
            timeout=self.timeout,
            **kwargs
        )

    def set_token(self, token):
        """Set authentication token as a cookie."""

        self.session.cookies.set("token", token)

    def set_basic_auth(self, username, password):
        """Configure HTTP Basic Authentication."""

        self.session.auth = (username, password)

    def close(self):
        """Close the HTTP session."""

        self.session.close()
