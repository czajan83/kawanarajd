from ..code.repository.recipes import RepRecipes
from .constants import db

def test_if_get_dishes_returns_dishes_list():
    # Given
    # When
    recipes = RepRecipes.get_recipes(db=db)
    # Then
    assert isinstance(recipes, list)
