import uuid
from typing import List, Type

from sqlalchemy.orm import Session

from code.database.models import Raws
from code.http.models import RawsResponseModel, RawsModel


def get_raws(db: Session) -> List[Type[RawsResponseModel]]:
    return db.query(Raws).all()

def get_raw(raw_id: str, db: Session) -> Type[RawsResponseModel]:
    return search_raw_by_id(raw_id, db)

def create_raw(body: RawsModel, db: Session) -> RawsResponseModel:
    raw = search_raw_by_name(body.name, db)
    if raw is None:
        id_raw = uuid.uuid4().hex
        raw = Raws(id=id_raw, name=body.name, kcal_100g=body.kcal_100g, fat=body.fat, saturated_fat=body.saturated_fat,
                   carbohydrates=body.carbohydrates, simple_sugars=body.simple_sugars, fiber=body.fiber,
                   proteins=body.proteins, salt=body.salt, cvi=body.cvi)
        db.add(raw)
        db.commit()
        db.refresh(raw)
    return raw

def update_raw(raw_id: str, body: RawsModel, db: Session) -> Type[RawsResponseModel] | int:
    raw = search_raw_by_id(raw_id, db)
    if raw is not None:
        if raw.name != body.name:
            return -2
        raw.kcal_100g=body.kcal_100g
        raw.fat=body.fat,
        raw.saturated_fat=body.saturated_fat
        raw.carbohydrates=body.carbohydrates
        raw.simple_sugars=body.simple_sugars
        raw.fiber=body.fiber
        raw.proteins=body.proteins
        raw.salt=body.salt
        raw.cvi=body.cvi
        db.commit()
        return raw
    return -1

def remove_raw(raw_id: str, body: RawsModel, db: Session) -> int | None:
    existing_raw = search_raw_by_id(raw_id, db)
    if existing_raw is not None:
        if existing_raw.name != body.name:
            return -2
        db.delete(existing_raw)
        db.commit()
        return 0
    return -1

def search_raw_by_name(raw_name: str, db: Session) -> Type[Raws] | None:
    existing_raws = db.query(Raws).all()
    for raw in existing_raws:
        if raw_name == raw.name:
            return raw
    return None

def search_raw_by_id(raw_id: str, db: Session):
    existing_raws = db.query(Raws).all()
    for raw in existing_raws:
        if raw_id == raw.id:
            return raw
    return None