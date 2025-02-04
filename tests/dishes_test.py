from ..code.repository.dishes import get_dishes
from .constants import db

def test_if_get_dishes_returns_dishes_list():
    # Given
    # When
    dishes = get_dishes(db=db)
    # Then
    assert isinstance(dishes, list)
