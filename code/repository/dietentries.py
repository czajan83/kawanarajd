import uuid
from datetime import datetime
from typing import List, Type

from sqlalchemy.orm import Session

from code.database.models import DietEntry
from code.http.models import DietEntryModel, DietEntryResponseModel


def get_dietentries(db: Session) -> List[Type[DietEntryResponseModel]]:
    return db.query(DietEntry).all()

def get_dietentry(dietentry_id: str, db: Session) -> Type[DietEntryResponseModel]:
    return search_dietentry(dietentry_id, db)

def create_dietentry(body: DietEntryModel, db: Session) -> DietEntryResponseModel | int:

    timestamp = validate_timestamp(body)
    if timestamp is None:
        return -3

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

def search_dietentry(dietentry_id: str, db: Session):
    existing_dietentries = db.query(DietEntry).all()
    for dietentry in existing_dietentries:
        if dietentry.id == dietentry_id:
            return dietentry
    return None

def validate_timestamp(body: DietEntryModel) -> str | None:
    try:
        timestamp = datetime.strptime(body.added_at, f"%Y-%m-%d %H:%M")
    except ValueError:
        if body.added_at == "":
            timestamp = datetime.now().strftime(f"%Y-%m-%d %H:%M")
        else:
            return None
    return timestamp