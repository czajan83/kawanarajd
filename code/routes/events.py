from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from code.database.database import get_db
from code.http.models import EventsModel, EventsResponseModel, EventsKawanarajdUpdate, EventsCoffeesServedUpdate
from code.repository import events as rep_events


router = APIRouter(prefix="/events", tags=["events"])


@router.get("/", response_model=List[EventsResponseModel])
def get_events(db: Session = Depends(get_db)):
    events = rep_events.get_events(db)
    if not events:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="events not found")
    return events


@router.get("/{event_id}", response_model=EventsResponseModel)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = rep_events.get_event(event_id, db)
    if event is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="event not found")
    return event


@router.post("/", response_model=EventsResponseModel, status_code=status.HTTP_201_CREATED)
def create_event(body: EventsModel, db: Session = Depends(get_db)):
    return rep_events.create_event(body, db)


@router.put("/{event_id}", response_model=EventsResponseModel)
def put_event(event_id: int, body: EventsModel, db: Session = Depends(get_db)):
    event = rep_events.update_event(event_id, body, db)
    if event == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="event not found")
    return event


@router.patch("/kawanarajd/{event_id}", response_model=EventsResponseModel)
def update_event_kawanarajd_status(body: EventsKawanarajdUpdate, event_id: int, db: Session = Depends(get_db)):
    event = rep_events.update_kawanarajd_status(event_id, body, db)
    if event == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="event not found")
    return event


@router.patch("/coffees_served/{event_id}", response_model=EventsResponseModel)
def update_event_coffees_served_status(body: EventsCoffeesServedUpdate, event_id: int, db: Session = Depends(get_db)):
    event = rep_events.update_coffees_served_status(event_id, body, db)
    if event == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="event not found")
    return event


@router.delete("/{event_id}", response_model=List[EventsResponseModel])
def delete_event(event_id: int, db: Session = Depends(get_db)):
    event = rep_events.remove_event(event_id, db)
    if event == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="event not found")
    return []