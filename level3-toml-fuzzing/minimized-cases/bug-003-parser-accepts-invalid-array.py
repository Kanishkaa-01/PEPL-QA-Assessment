import toml
import tomllib

document = 'name = [1, 2,'

print("Input:", repr(document))

print("\nThird-party parser:")
try:
    print(toml.loads(document))
except Exception as error:
    print(type(error).__name__, error)

print("\nBuilt-in parser:")
try:
    print(tomllib.loads(document))
except Exception as error:
    print(type(error).__name__, error)