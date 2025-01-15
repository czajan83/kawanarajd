import uuid
from fastapi import APIRouter

router = APIRouter()

@router.get("/raws")
def get_raws():
    idRaw = uuid.uuid4().hex
    return [{"id":idRaw, "name": "buckwheat_groats", "kcal/100g": 347, "fat": 3.7, "saturated": 0.6, "carbohydrates": 63, "simple_sugars": 0.7, "fiber": 5.9, "proteins": 14, "salt": 0.1, "cvi": 2.17}, ]