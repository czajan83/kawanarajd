from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from code.database.database import get_db
from code.http.models import RawsModel, RawsResponseModel
from code.repository import raws as rep_raws

router = APIRouter(prefix="/raws", tags=["raws"])

@router.get("/", response_model=List[RawsResponseModel])
def get_raws(db: Session = Depends(get_db)):
    raws = rep_raws.get_raws(db)
    if not raws:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="raws not found")
    return raws

@router.post("/", response_model=RawsResponseModel, status_code=status.HTTP_201_CREATED)
def create_raw(body: RawsModel, db: Session = Depends(get_db)):
    return rep_raws.create_raw(body, db)