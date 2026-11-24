import toml

data = {'0\x1f': 0}

serialized = toml.dumps(data)
deserialized = toml.loads(serialized)

print("Original:", repr(data))
print("Serialized:", repr(serialized))
print("Parsed:", repr(deserialized))

assert deserialized == data