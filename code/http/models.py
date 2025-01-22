from datetime import datetime, date
from typing import List

from pydantic import BaseModel, Field


class DishesModel(BaseModel):
    name: str = Field(max_length=96)
    kcal_100g: float
    fat: float
    saturated_fat: float
    carbohydrates: float
    simple_sugars: float
    fiber: float
    proteins: float
    salt: float

class DishesResponseModel(DishesModel):
    id: int

class RecipesModel(BaseModel):
    name: str = Field(max_length=96)
    recipe_ids: List[int]
    recipe_amounts: List[int]

class MealDEModel(BaseModel):
    added_at: datetime
    food_id: int
    food_amount_in_grams: float

class MeasurementDEModel(BaseModel):
    added_at: datetime
    weight_in_kilograms: float

class ActivityDEModel(BaseModel):
    added_at: datetime
    distance_in_kilometers: float

class DEResponseModel(BaseModel):
    id: int
    added_at: datetime
    entry_type: str
    food_id: int
    food_amount_in_grams: float
    weight_in_kilograms: float
    distance_in_kilometers: float

class EventsModel(BaseModel):
    event_at: date
    organizer_name: str
    event_name: str
    kawanarajd: bool
    coffees_served: int

class EventsResponseModel(EventsModel):
    id: int

class EventsKawanarajdUpdate(BaseModel):
    kawanarajd: bool

class EventsCoffeesServedUpdate(BaseModel):
    coffees_served: int