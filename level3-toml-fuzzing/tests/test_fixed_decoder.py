import pytest
import tomllib

from fixes.fixed_decoder import parse_array


def test_fix_bug_003_incomplete_array():
    with pytest.raises(ValueError):
        parse_array("[1, 2,")


def test_fix_bug_005_empty_incomplete_array():
    with pytest.raises(ValueError):
        parse_array("[")


def test_valid_array_is_accepted():
    result = parse_array("[1, 2, 3]")
    assert tomllib.loads(f"values = {result}") == {
        "values": [1, 2, 3]
    }
