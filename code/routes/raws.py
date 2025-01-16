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

@router.get("/{raw_id}", response_model=RawsResponseModel)
def get_raw(raw_id: str, db: Session = Depends(get_db)):
    raw = rep_raws.get_raw(raw_id, db)
    if raw is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="raw not found")
    return raw

@router.post("/", response_model=RawsResponseModel, status_code=status.HTTP_201_CREATED)
def create_raw(body: RawsModel, db: Session = Depends(get_db)):
    return rep_raws.create_raw(body, db)

@router.put("/{raw_id}", response_model=RawsResponseModel)
def put_raw(raw_id: str, body: RawsModel, db: Session = Depends(get_db)):
    raw = rep_raws.update_raw(raw_id, body, db)
    if raw == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="raw not found")
    if raw == -2:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="raw name incorrect")
    return raw

@router.delete("/{raw_id}", response_model=List[RawsResponseModel])
def delete_raw(raw_id: str, body: RawsModel, db: Session = Depends(get_db)):
    raw = rep_raws.remove_raw(raw_id, body, db)
    if raw == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="raw not found")
    if raw == -2:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="raw name incorrect")
    return []