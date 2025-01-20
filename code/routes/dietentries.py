from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from code.database.database import get_db
from code.http.models import DietEntryModel, DietEntryResponseModel
from code.repository import dietentries as rep_dietentries

router = APIRouter(prefix="/dietentries", tags=["dietentries"])

@router.get("/", response_model=List[DietEntryResponseModel])
def get_raws(db: Session = Depends(get_db)):
    raws = rep_dietentries.get_dietentries(db)
    if not raws:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="diet entries not found")
    return raws

@router.get("/{dietentry_id}", response_model=DietEntryResponseModel)
def get_raw(raw_id: str, db: Session = Depends(get_db)):
    raw = rep_dietentries.get_dietentry(raw_id, db)
    if raw is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="diet entry not found")
    return raw

@router.post("/", response_model=DietEntryResponseModel, status_code=status.HTTP_201_CREATED)
def create_raw(body: DietEntryModel, db: Session = Depends(get_db)):
    dietentry = rep_dietentries.create_dietentry(body, db)
    if dietentry == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="raw not found, please check your food_id")
    if dietentry == -2:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"sauce not found, please check your food_id")
    if dietentry == -3:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"added_at format incorrect, please use the %Y-%m-%d %H:%M format "
                                   f"or left it blank if use datetime.now() func")
    return dietentry

# @router.put("/{raw_id}", response_model=RawsResponseModel)
# def put_raw(raw_id: str, body: RawsModel, db: Session = Depends(get_db)):
#     raw = rep_raws.update_raw(raw_id, body, db)
#     if raw == -1:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="raw not found")
#     if raw == -2:
#         raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="raw name incorrect")
#     return raw
#
# @router.delete("/{raw_id}", response_model=List[RawsResponseModel])
# def delete_raw(raw_id: str, body: RawsModel, db: Session = Depends(get_db)):
#     raw = rep_raws.remove_raw(raw_id, body, db)
#     if raw == -1:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="raw not found")
#     if raw == -2:
#         raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="raw name incorrect")
#     return []