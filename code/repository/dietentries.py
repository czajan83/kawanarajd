import uuid
from datetime import datetime
from typing import List, Type

from sqlalchemy.orm import Session

from code.database.models import DietEntry
from code.http.models import DietEntryModel, DietEntryResponseModel
from code.repository import raws as rep_raws
from code.repository import sauces as rep_sauces


def get_dietentries(db: Session) -> List[Type[DietEntryResponseModel]]:
    return db.query(DietEntry).all()

def get_dietentry(dietentry_id: str, db: Session) -> Type[DietEntryResponseModel]:
    return search_dietentry(dietentry_id, db)

def create_dietentry(body: DietEntryModel, db: Session) -> DietEntryResponseModel | int:

    if body.entry_type == f"raw":
        if rep_raws.search_raw_by_id(body.food_id, db) is None:
            return -1
    if body.entry_type == f"sauce":
        if rep_sauces.search_sauce_by_id(body.food_id, db) is None:
            return -1

    try:
        timestamp = datetime.strptime(body.added_at, f"%Y-%m-%d %H:%M")
    except ValueError:
        if body.added_at == "":
            timestamp = datetime.now().strftime(f"%Y-%m-%d %H:%M")
        else:
            return -2

    id_dietentry = uuid.uuid4().hex
    dietentry = DietEntry(id=id_dietentry,
                          added_at=timestamp,
                          entry_type=body.entry_type,
                          food_id=body.food_id,
                          food_amount_in_grams=body.food_amount_in_grams,
                          weight_in_kilograms=body.weight_in_kilograms
    )
    db.add(dietentry)
    db.commit()
    db.refresh(dietentry)
    return dietentry
#
# def update_raw(raw_id: str, body: RawsModel, db: Session) -> Type[RawsResponseModel] | int:
#     raw = search_raw_by_id(raw_id, db)
#     if raw is not None:
#         if raw.name != body.name:
#             return -2
#         raw.kcal_100g=body.kcal_100g
#         raw.fat=body.fat,
#         raw.saturated_fat=body.saturated_fat
#         raw.carbohydrates=body.carbohydrates
#         raw.simple_sugars=body.simple_sugars
#         raw.fiber=body.fiber
#         raw.proteins=body.proteins
#         raw.salt=body.salt
#         raw.cvi=body.cvi
#         db.commit()
#         return raw
#     return -1
#
# def remove_raw(raw_id: str, body: RawsModel, db: Session) -> int | None:
#     existing_raw = search_raw_by_id(raw_id, db)
#     if existing_raw is not None:
#         if existing_raw.name != body.name:
#             return -2
#         db.delete(existing_raw)
#         db.commit()
#         return 0
#     return -1
#
# def search_raw_by_name(raw_name: str, db: Session) -> Type[Raws] | None:
#     existing_raws = db.query(Raws).all()
#     for raw in existing_raws:
#         if raw_name == raw.name:
#             return raw
#     return None
#
def search_dietentry(dietentry_id: str, db: Session):
    existing_dietentries = db.query(DietEntry).all()
    for dietentry in existing_dietentries:
        if dietentry.id == dietentry_id:
            return dietentry
    return None