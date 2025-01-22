from typing import List, Type

from sqlalchemy.orm import Session

from code.database.models import Events
from code.http.models import EventsResponseModel, EventsModel


def get_events(db: Session) -> List[Type[EventsResponseModel]]:
    return db.query(Events).all()

def get_event(event_id: int, db: Session) -> Type[EventsResponseModel]:
    return search_event(event_id, db)

def create_event(body: EventsModel, db: Session) -> EventsResponseModel:
    event = Events(event_at=body.event_at,
                   organizer_name=body.organizer_name,
                   event_name=body.event_name,
                   kawanarajd=body.kawanarajd,
                   coffees_served=body.coffees_served)
    db.add(event)
    db.commit()
    db.refresh(event)
    return event

def update_event(event_id: int, body: EventsModel, db: Session) -> Type[EventsResponseModel] | int:
    event = search_event(event_id, db)
    if event is None:
        return -1
    event.event_at = body.event_at
    event.organizer_name = body.organizer_name
    event.event_name = body.event_name
    event.kawanarajd = body.kawanarajd
    event.coffees_served = body.coffees_served
    db.commit()
    return event

def remove_event(event_id: int, db: Session) -> int | None:
    event = search_event(event_id, db)
    if event is None:
        return -1
    db.delete(event)
    db.commit()
    return None

def search_event(event_id: int, db: Session) -> Type[Events] | None:
    events = db.query(Events).all()
    for event in events:
        if event_id == event.id:
            return event
    return None