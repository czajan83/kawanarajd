from sqlalchemy.orm import Session
from ..code.database.database import engine

db = Session(autocommit=False, autoflush=False, bind=engine)