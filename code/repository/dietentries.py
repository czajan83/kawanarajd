from typing import List, Type

from sqlalchemy.orm import Session

from code.database.models import DietEntry
from code.http.models import MealDEModel, MeasurementDEModel, ActivityDEModel, DEResponseModel

from code.repository import dishes as rep_dishes


def get_dietentries(db: Session) -> List[Type[DEResponseModel]]:
    return db.query(DietEntry).all()

def get_dietentry(dietentry_id: int, db: Session) -> Type[DEResponseModel]:
    return search_dietentry(dietentry_id, db)

def create_meal(body: MealDEModel, db: Session) -> DEResponseModel | int:
    dish = rep_dishes.search_dish_by_id(body.food_id, db)
    if dish is None:
        return -1
    meal = DietEntry(added_at=body.added_at,
                     entry_type="meal",
                     food_id=body.food_id,
                     food_amount_in_grams=body.food_amount_in_grams,
                     weight_in_kilograms=0,
                     distance_in_kilometers=0
                     )
    return save_in_db(meal, db)

def update_meal(dietentry_id: int, body: MealDEModel, db: Session) -> Type[DietEntry] | int:
    dietentry = search_dietentry(dietentry_id=dietentry_id, db=db)
    dish = rep_dishes.search_dish_by_id(body.food_id, db)
    if dietentry is None:
        return -2
    if dietentry.entry_type != "meal":
        return -3
    if dish is None:
        return -1
    dietentry.added_at = body.added_at
    dietentry.food_id = body.food_id
    dietentry.food_amount_in_grams = body.food_amount_in_grams
    db.commit()
    return dietentry

def create_measurement(body: MeasurementDEModel, db: Session) -> DEResponseModel | int:
    measurement_dish = rep_dishes.search_dish_by_name("measurement", db)
    if measurement_dish is None:
        return -1
    measurement = DietEntry(added_at=body.added_at,
                            entry_type="measurement",
                            food_id=measurement_dish.id,
                            food_amount_in_grams=0,
                            weight_in_kilograms=body.weight_in_kilograms,
                            distance_in_kilometers=0)
    return save_in_db(measurement, db)

def update_measurement(dietentry_id: int, body: MeasurementDEModel, db: Session) -> Type[DietEntry] | int:
    dietentry = search_dietentry(dietentry_id=dietentry_id, db=db)
    measurement_dish = rep_dishes.search_dish_by_name("measurement", db)
    if dietentry is None:
        return -2
    if dietentry.entry_type != "measurement":
        return -3
    if measurement_dish is None:
        return -1
    dietentry.added_at = body.added_at
    dietentry.weight_in_kilograms = body.weight_in_kilograms
    db.commit()
    return dietentry

def create_activity(body: ActivityDEModel, db: Session) -> DEResponseModel | int:
    activity_dish = rep_dishes.search_dish_by_name("activity", db)
    if activity_dish is None:
        return -1
    activity = DietEntry(added_at=body.added_at,
                         entry_type="activity",
                         food_id=activity_dish.id,
                         food_amount_in_grams=0,
                         weight_in_kilograms=0,
                         distance_in_kilometers=body.distance_in_kilometers)
    return save_in_db(activity, db)

def update_activity(dietentry_id: int, body: ActivityDEModel, db: Session) -> Type[DietEntry] | int:
    dietentry = search_dietentry(dietentry_id=dietentry_id, db=db)
    activity_dish = rep_dishes.search_dish_by_name("activity", db)
    if dietentry is None:
        return -2
    if dietentry.entry_type != "activity":
        return -3
    if activity_dish is None:
        return -1
    dietentry.added_at = body.added_at
    dietentry.distance_in_kilometers = body.distance_in_kilometers
    db.commit()
    return dietentry

def remove_dietentry(dietentry_id: int, db: Session) -> int | None:
    dietentry = search_dietentry(dietentry_id, db)
    if dietentry is None:
        return None
    db.delete(dietentry)
    db.commit()
    return 0

def search_dietentry(dietentry_id: int, db: Session) -> Type[DietEntry] | None:
    existing_dietentries = db.query(DietEntry).all()
    for dietentry in existing_dietentries:
        if dietentry.id == dietentry_id:
            return dietentry
    return None

def save_in_db(dietentry: DietEntry, db: Session) -> DEResponseModel:
    db.add(dietentry)
    db.commit()
    db.refresh(dietentry)
    return dietentry
