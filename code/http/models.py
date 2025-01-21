from typing import List

from pydantic import BaseModel, Field


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

class RecipesModel(BaseModel):
    name: str = Field(max_length=96)
    recipe_ids: List[int]
    recipe_amounts: List[int]

