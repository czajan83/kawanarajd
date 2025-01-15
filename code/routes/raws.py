import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from code.database.database import get_db
from code.repository import raws as rep_raws

router = APIRouter(prefix="/raws", tags=["raws"])

@router.get("/")
def get_raws(db: Session = Depends(get_db)):
    raws = rep_raws.get_raws(db)
    return raws
    # idRaw = uuid.uuid4().hex
    # return [{"id":idRaw, "name": "buckwheat_groats", "kcal/100g": 347, "fat": 3.7, "saturated": 0.6, "carbohydrates": 63, "simple_sugars": 0.7, "fiber": 5.9, "proteins": 14, "salt": 0.1, "cvi": 2.17}, ]