
def encode_toml_string(value):
    """Encode a Python string as a valid TOML basic string."""

    escaped = (
        value.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\b", "\\b")
        .replace("\t", "\\t")
        .replace("\n", "\\n")
        .replace("\f", "\\f")
        .replace("\r", "\\r")
    )

    result = []

    for char in escaped:
        code = ord(char)

        if code < 32 or code == 127:
            result.append(f"\\u{code:04X}")
        else:
            result.append(char)

    return '"' + "".join(result) + '"'
