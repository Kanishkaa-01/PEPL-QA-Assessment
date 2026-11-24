
import pytest
import toml
import tomllib


@pytest.mark.xfail(
    reason="BUG-001: Encoder corrupts control characters in keys",
    strict=True
)
def test_bug_001_control_character_key_corruption():
    data = {'0\x1f': 0}
    serialized = toml.dumps(data)
    assert toml.loads(serialized) == data


@pytest.mark.xfail(
    reason="BUG-002: Encoder crashes on control characters in keys",
    strict=True
)
def test_bug_002_encoder_crash():
    data = {'\x1f': 0}
    serialized = toml.dumps(data)
    assert toml.loads(serialized) == data


@pytest.mark.xfail(
    reason="BUG-003: Decoder accepts incomplete arrays",
    strict=True
)
def test_bug_003_incomplete_array():
    with pytest.raises(ValueError):
        toml.loads('name = [1, 2,')


@pytest.mark.xfail(
    reason="BUG-004: Decoder accepts incomplete inline tables",
    strict=True
)
def test_bug_004_incomplete_inline_table():
    with pytest.raises(ValueError):
        toml.loads('key = {')


@pytest.mark.xfail(
    reason="BUG-005: Decoder accepts incomplete arrays",
    strict=True
)
def test_bug_005_incomplete_array():
    with pytest.raises(ValueError):
        toml.loads('array = [')
