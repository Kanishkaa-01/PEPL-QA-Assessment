
import string
import toml

from hypothesis import given, settings, strategies as st


toml_keys = st.text(
    alphabet=string.ascii_letters + string.digits + "_-",
    min_size=1,
    max_size=10
)

toml_values = st.one_of(
    st.integers(),
    st.text(
        alphabet=string.ascii_letters + string.digits + " _-",
        max_size=30
    ),
    st.booleans(),
    st.floats(allow_nan=False, allow_infinity=False)
)

toml_documents = st.dictionaries(
    keys=toml_keys,
    values=toml_values,
    min_size=1,
    max_size=10
)


@settings(max_examples=100)
@given(data=toml_documents)
def test_toml_roundtrip(data):
    serialized = toml.dumps(data)
    deserialized = toml.loads(serialized)

    assert deserialized == data
