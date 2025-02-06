import pytest
from fastapi import HTTPException

from ..code.database.models import Dishes
from ..code.http.models import DishesModel
from ..code.repository import dishes as rep_dish
from ..code.routes import dishes as route_dish
from .constants import db

dish_id = 0
dishes_amount = 0

def test_if_get_dishes_returns_list():
    # Given

    # When
    dishes = rep_dish.get_dishes(db=db)
    global dishes_amount
    dishes_amount = len(dishes)

    # Then
    assert isinstance(dishes, list)

def test_if_create_dish_returns_dishes_response_model():
    # Given
    dish = DishesModel(name="aaa")

    # When
    new_dish = rep_dish.create_dish(dish, db)
    global dish_id
    dish_id = new_dish.id

    # Then
    assert isinstance(new_dish, Dishes)

def test_if_new_dish_has_id_int_type():
    assert isinstance(dish_id, int)

def test_if_get_dish_returns_newly_added_dish_id():
    # When
    dish = rep_dish.get_dish(dish_id, db)

    # Then
    assert dish.id == dish_id

def test_if_get_dishes_returns_one_dish_more_than_previously():
    # When
    dishes = rep_dish.get_dishes(db=db)

    # Then
    assert len(dishes) == dishes_amount + 1

def test_if_update_dish_returns_dishes_response_model():
    # Given
    dish = DishesModel(name="aaa", kcal_100g=1)

    # When
    new_dish = rep_dish.update_dish(dish_id, dish, db)

    # Then
    assert isinstance(new_dish, Dishes)

def test_if_get_dishes_returns_same_amount_of_dishes_as_before_update():
    # When
    dishes = rep_dish.get_dishes(db=db)
    # Then
    assert len(dishes) == dishes_amount + 1

def test_if_dish_has_been_updated_correctly():
    # When
    dish = rep_dish.get_dish(dish_id, db=db)
    # Then
    assert dish.kcal_100g == 1

def test_if_remove_dish_returns_0():
    # Given
    dish = DishesModel(name="aaa")

    # When
    return_value = rep_dish.remove_dish(dish_id, dish, db)

    # Then
    assert return_value == 0

def test_if_dish_has_been_truly_removed():
    # When
    dishes = rep_dish.get_dishes(db=db)
    # Then
    assert len(dishes) == dishes_amount

def test_if_route_get_dishes_returns_list():
    # Given

    # When
    dishes = route_dish.get_dishes(db=db)
    global dishes_amount
    dishes_amount = len(dishes)

    # Then
    assert isinstance(dishes, list)

def test_if_route_create_dish_returns_dishes_response_model():
    # Given
    dish = DishesModel(name="aaa")

    # When
    new_dish = route_dish.create_dish(dish, db)
    global dish_id
    dish_id = new_dish.id

    # Then
    assert isinstance(new_dish, Dishes)

def test_if_route_new_dish_has_id_int_type():
    assert isinstance(dish_id, int)

def test_if_route_get_dish_returns_newly_added_dish_id():
    # When
    dish = route_dish.get_dish(dish_id, db)

    # Then
    assert dish.id == dish_id

def test_if_delete_dish_returns_empty_list():
    # Given
    dish = DishesModel(name="aaa")

    # When
    return_value = route_dish.delete_dish(dish_id, dish, db)

    # Then
    assert return_value == []

def test_if_dish_has_been_truly_removed_by_route_function():
    # When
    dishes = route_dish.get_dishes(db=db)
    # Then
    assert len(dishes) == dishes_amount

def test_if_get_non_existent_dish_throws_exception():
    # When
    with pytest.raises(HTTPException) as error:
        route_dish.get_dish(dish_id, db)

    # Then
    assert str(error.value) == "404: dish not found"