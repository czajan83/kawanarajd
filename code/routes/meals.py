from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from code.database.database import get_db
from code.http.models import MealDEModel, DEResponseModel
from code.repository import dietentries as rep_dietentries

router = APIRouter(prefix="/meals", tags=["meals"])

@router.post("/", response_model=DEResponseModel, status_code=status.HTTP_201_CREATED)
def create_meal(body: MealDEModel, db: Session = Depends(get_db)):
    dietentry = rep_dietentries.add_meal(body, db)
    if dietentry == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="dish not found, please check your food_id")
    return dietentry

@router.put("/{dietentry_id}", response_model=DEResponseModel)
def create_meal(dietentry_id: int, body: MealDEModel, db: Session = Depends(get_db)):
    dietentry = rep_dietentries.update_meal(dietentry_id, body, db)
    if dietentry == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="dish not found, please check your food_id")
    if dietentry == -2:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="dietentry not found, please check your dietentry_id")
    if dietentry == -3:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="dietentry name incorrect")
    return dietentry