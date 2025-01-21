from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from code.database.database import get_db
from code.http.models import MealDEModel, MeasurementDEModel, ActivityDEModel, DEResponseModel
from code.repository import dietentries as rep_dietentries

router = APIRouter(prefix="/dietentries", tags=["dietentries"])

@router.get("/", response_model=List[DEResponseModel])
def get_dietentries(db: Session = Depends(get_db)):
    dietentries = rep_dietentries.get_dietentries(db)
    if not dietentries:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="dietentries not found")
    return dietentries

@router.get("/{dietentry_id}", response_model=DEResponseModel)
def get_dietentry(dietentry_id: int, db: Session = Depends(get_db)):
    dietentry = rep_dietentries.get_dietentry(dietentry_id, db)
    if dietentry is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="dietentry not found")
    return dietentry
