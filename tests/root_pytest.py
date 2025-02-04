from ..code.routes.root import root


def test_if_root_returns_hello_world():
    # Given
    expected_value = {"message": "Hello World!!!"}
    # When
    aaa = root()
    #Then
    assert aaa == expected_value