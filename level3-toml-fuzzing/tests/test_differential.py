
import toml
import tomllib

from hypothesis import given, settings, strategies as st


# Known defect already documented as BUG-003.
KNOWN_FAILURES = {
    'name = [1, 2,',
    'key = {',
    'array = [',
}


# Generate valid TOML documents.
valid_documents = st.dictionaries(
    keys=st.text(
        alphabet="abcdefghijklmnopqrstuvwxyz",
        min_size=1,
        max_size=8
    ),
    values=st.one_of(
        st.integers(),
        st.text(
            alphabet="abcdefghijklmnopqrstuvwxyz 0123456789",
            max_size=20
        ),
        st.booleans()
    ),
    min_size=1,
    max_size=5
).map(toml.dumps)


# Generate malformed TOML documents.
invalid_documents = st.sampled_from([
    'name = ',
    'name = "unfinished',
    'name = 123\nname = 456',
    '[section\nvalue = 10',
    'value = truee',
    'name: "John"',
    'name = [1, 2,',
    'name = {key = 1',
    'array = [',
    'number = 01',
    'value = 1.2.3',
    'date = 2024-13-40',
    'name = "hello\nworld"',
    'key = {',
    '[[products]'
])


# Generate additional arbitrary TOML-like text.
arbitrary_documents = st.text(
    alphabet="abcdefghijklmnopqrstuvwxyz"
             "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
             "0123456789"
             ' =[]{},".:_\n-',
    min_size=1,
    max_size=100
)


# Combine generators and exclude the known failure.
toml_texts = st.one_of(
    valid_documents,
    invalid_documents,
    arbitrary_documents
).filter(lambda document: document not in KNOWN_FAILURES)


@settings(max_examples=300, deadline=None)
@given(document=toml_texts)
def test_toml_parsers_agree(document):

    toml_result = None
    tomllib_result = None

    toml_error = None
    tomllib_error = None

    # Parse using the third-party TOML library.
    try:
        toml_result = toml.loads(document)
    except Exception as error:
        toml_error = type(error)

    # Parse using Python's built-in TOML parser.
    try:
        tomllib_result = tomllib.loads(document)
    except Exception as error:
        tomllib_error = type(error)

    # Both parsers should agree on acceptance or rejection.
    assert (toml_error is None) == (tomllib_error is None), (
        f"Parsers disagree on acceptance.\n"
        f"Document: {document!r}\n"
        f"toml error: {toml_error}\n"
        f"tomllib error: {tomllib_error}"
    )

    # If both accept, their results should match.
    if toml_error is None and tomllib_error is None:
        assert toml_result == tomllib_result, (
            f"Parsers returned different results.\n"
            f"Document: {document!r}\n"
            f"toml result: {toml_result!r}\n"
            f"tomllib result: {tomllib_result!r}"
        )
