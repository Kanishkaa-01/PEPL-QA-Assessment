
def parse_array(value):
    """
    Validate that a TOML array has its closing bracket
    before parsing it.
    """
    value = value.strip()

    if not value.startswith("["):
        raise ValueError("Invalid TOML array: missing opening bracket")

    if not value.endswith("]"):
        raise ValueError("Invalid TOML array: missing closing bracket")

    return value
