import uuid
from typing import List, Type

from sqlalchemy.orm import Session

from code.database.models import Raws
from code.http.models import RawsResponseModel, RawsModel


def get_raws(db: Session) -> List[Type[RawsResponseModel]]:
    return db.query(Raws).all()

def create_raw(body: RawsModel, db: Session) -> RawsResponseModel:
    raw = search_raw(body, db)
    if raw is None:
        id_raw = uuid.uuid4().hex
        raw = Raws(id=id_raw, name=body.name, kcal_100g=body.kcal_100g, fat=body.fat, saturated_fat=body.saturated_fat, carbohydrates=body.carbohydrates, simple_sugars=body.simple_sugars, fiber=body.fiber, proteins=body.proteins, salt=body.salt, cvi=body.cvi)
        db.add(raw)
        db.commit()
        db.refresh(raw)
    return raw

def search_raw(body: RawsModel, db: Session) -> Type[Raws] | None:
    existing_raws = db.query(Raws).all()
    for raw in existing_raws:
        if body.name == raw.name:
            return raw
    return None