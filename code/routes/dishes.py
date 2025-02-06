from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from ..database.database import get_db
from ..http.models import DishesModel, DishesResponseModel
from ..repository import dishes as rep_dishes

router = APIRouter(prefix="/dishes", tags=["dishes"])

@router.get("/", response_model=List[DishesResponseModel])
def get_dishes(db: Session = Depends(get_db)):
    dishes = rep_dishes.get_dishes(db)
    if not dishes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="dishes not found")
    return dishes

@router.get("/{dish_id}", response_model=DishesResponseModel)
def get_dish(dish_id: int, db: Session = Depends(get_db)):
    dish = rep_dishes.get_dish(dish_id, db)
    if dish is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="dish not found")
    return dish

@router.post("/", response_model=DishesResponseModel, status_code=status.HTTP_201_CREATED)
def create_dish(body: DishesModel, db: Session = Depends(get_db)):
    return rep_dishes.create_dish(body, db)

@router.put("/{dish_id}", response_model=DishesResponseModel)
def put_dish(dish_id: int, body: DishesModel, db: Session = Depends(get_db)):
    dish = rep_dishes.update_dish(dish_id, body, db)
    if dish == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="dish not found")
    if dish == -2:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="dish name incorrect")
    return dish

@router.delete("/{dish_id}", response_model=List[DishesResponseModel])
def delete_dish(dish_id: int, body: DishesModel, db: Session = Depends(get_db)):
    dish = rep_dishes.remove_dish(dish_id, body, db)
    if dish == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="dish not found")
    if dish == -2:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="dish name incorrect")
    return []