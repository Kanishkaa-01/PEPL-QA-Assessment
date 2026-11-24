import toml

data = {'\x1f': 0}

print("Original:", repr(data))
print("Serialized:", repr(toml.dumps(data)))