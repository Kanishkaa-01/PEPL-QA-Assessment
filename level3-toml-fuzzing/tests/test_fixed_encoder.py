import tomllib
from fixes.fixed_encoder import encode_toml_string


def test_fix_bug_001_control_character_key():
    original_key = '0\x1f'

    encoded_key = encode_toml_string(original_key)
    document = f'{encoded_key} = 0'

    parsed = tomllib.loads(document)

    assert list(parsed.keys()) == [original_key]


def test_fix_bug_002_encoder_crash():
    original_key = '\x1f'

    encoded_key = encode_toml_string(original_key)
    document = f'{encoded_key} = 0'

    parsed = tomllib.loads(document)

    assert list(parsed.keys()) == [original_key]


def test_fix_common_control_characters():
    original = 'Hello\nWorld\tTest'

    encoded = encode_toml_string(original)
    parsed = tomllib.loads(f'value = {encoded}')

    assert parsed['value'] == original
