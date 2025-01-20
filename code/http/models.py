from typing import List

from datetime import datetime
from pydantic import BaseModel, Field


class Ingredient(BaseModel):
    id: str
    amount_in_grams: float
    class Config:
        orm_mode = True

class SaucesModel(BaseModel):
    name: str = Field(max_length=96)
    ingredients: List[Ingredient]
    final_amount_in_grams: float
    class Config:
        arbitrary_types_allowed = True

class SaucesResponseModel(SaucesModel):
    id: str

class DietEntryModel(BaseModel):
    added_at: str
    entry_type: str
    food_id: str
    food_amount_in_grams: float
    weight_in_kilograms: float

class DietEntryResponseModel(DietEntryModel):
    id: str

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