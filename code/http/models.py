from pydantic import BaseModel, Field


class RawsModel(BaseModel):
    name: str = Field(max_length=96)
    kcal_100g: float
    fat: float
    saturated_fat: float
    carbohydrates: float
    simple_sugars: float
    fiber: float
    proteins: float
    salt: float
    cvi: float

class RawsResponseModel(RawsModel):
    id: str
    class Config:
        orm_mode=True
