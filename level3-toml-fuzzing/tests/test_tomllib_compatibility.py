import string
import toml
import tomllib

from hypothesis import given, settings, strategies as st


# Generate safe TOML-compatible dictionary keys.
toml_keys = st.text(
    alphabet=string.ascii_letters + string.digits + "_-",
    min_size=1,
    max_size=10
)

# Generate simple TOML-compatible values.
toml_values = st.one_of(
    st.integers(),
    st.text(
        alphabet=string.ascii_letters + string.digits + " _-",
        max_size=30
    ),
    st.booleans(),
    st.floats(
        allow_nan=False,
        allow_infinity=False
    )
)

# Generate dictionaries containing these keys and values.
toml_documents = st.dictionaries(
    keys=toml_keys,
    values=toml_values,
    min_size=1,
    max_size=10
)


@settings(max_examples=100)
@given(data=toml_documents)
def test_toml_output_is_compatible_with_tomllib(data):
    """
    Property 2:
    TOML written by toml.dumps() should be readable
    by Python's built-in tomllib parser.
    """

    serialized = toml.dumps(data)

    parsed_by_toml = toml.loads(serialized)
    parsed_by_tomllib = tomllib.loads(serialized)

    assert parsed_by_tomllib == data
    assert parsed_by_tomllib == parsed_by_toml