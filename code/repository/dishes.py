from typing import List, Type

from sqlalchemy.orm import Session

from ..database.models import Dishes
from ..http.models import DishesResponseModel, DishesModel


def get_dishes(db: Session) -> List[Type[DishesResponseModel]]:
    return db.query(Dishes).all()

def get_dish(dish_id: int, db: Session) -> Type[DishesResponseModel]:
    return search_dish_by_id(dish_id, db)

def create_dish(body: DishesModel, db: Session) -> DishesResponseModel:
    dish = search_dish_by_name(body.name, db)
    if dish is None:
        dish = Dishes(name=body.name,
                     kcal_100g=body.kcal_100g,
                     fat=body.fat,
                     saturated_fat=body.saturated_fat,
                     carbohydrates=body.carbohydrates,
                     simple_sugars=body.simple_sugars,
                     fiber=body.fiber,
                     proteins=body.proteins,
                     salt=body.salt)
        db.add(dish)
        db.commit()
        db.refresh(dish)
    return dish

def update_dish(dish_id: int, body: DishesModel, db: Session) -> Type[DishesResponseModel] | int:
    dish = search_dish_by_id(dish_id, db)
    if dish is not None:
        if dish.name != body.name:
            return -2
        dish.kcal_100g=body.kcal_100g
        dish.fat=body.fat,
        dish.saturated_fat=body.saturated_fat
        dish.carbohydrates=body.carbohydrates
        dish.simple_sugars=body.simple_sugars
        dish.fiber=body.fiber
        dish.proteins=body.proteins
        dish.salt=body.salt
        db.commit()
        return dish
    return -1

def remove_dish(dish_id: int, body: DishesModel, db: Session) -> int | None:
    existing_dish = search_dish_by_id(dish_id, db)
    if existing_dish is not None:
        if existing_dish.name != body.name:
            return -2
        db.delete(existing_dish)
        db.commit()
        return 0
    return -1

def search_dish_by_name(dish_name: str, db: Session) -> Type[Dishes] | None:
    existing_dishes = db.query(Dishes).all()
    for dish in existing_dishes:
        if dish_name == dish.name:
            return dish
    return None

def search_dish_by_id(dish_id: int, db: Session) -> Type[Dishes] | None:
    existing_dishes = db.query(Dishes).all()
    for dish in existing_dishes:
        if dish_id == dish.id:
            return dish
    return None