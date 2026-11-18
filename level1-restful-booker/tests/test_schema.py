import json

from pathlib import Path
from jsonschema import validate


def test_booking_response_schema(api_client, booking_id):

    response = api_client.get(
        f"/booking/{booking_id}"
    )

    assert response.status_code == 200

    schema_path = (
        Path(__file__).parent.parent
        / "schemas"
        / "booking_schema.json"
    )

    with open(schema_path, "r") as file:
        schema = json.load(file)

    validate(
        instance=response.json(),
        schema=schema
    )
