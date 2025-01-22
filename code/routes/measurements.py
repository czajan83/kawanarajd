from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from code.database.database import get_db
from code.http.models import MeasurementDEModel, DEResponseModel
from code.repository import dietentries as rep_dietentries

router = APIRouter(prefix="/measurements", tags=["measurements"])

@router.post("/", response_model=DEResponseModel, status_code=status.HTTP_201_CREATED)
def create_measurement(body: MeasurementDEModel, db: Session = Depends(get_db)):
    dietentry = rep_dietentries.create_measurement(body, db)
    if dietentry == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="dish not found, please check your food_id")
    return dietentry

@router.put("/{dietentry_id}", response_model=DEResponseModel)
def update_measurement(dietentry_id: int, body: MeasurementDEModel, db: Session = Depends(get_db)):
    dietentry = rep_dietentries.update_measurement(dietentry_id, body, db)
    if dietentry == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="\"measurement\" dish not found, "
                                   "please add special \"measurement,0,0,0,0,0,0,0\" entry to dishes database ")
    if dietentry == -2:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="dietentry not found")
    if dietentry == -3:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="dietentry name incorrect, "
                                   "please make sure that you try to edit \"measurement\" dietentry_id")
    return dietentry