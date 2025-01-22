from sqlalchemy import Column, String, Float, ForeignKey, Integer, DateTime, func, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dishes(Base):
    __tablename__ = "dishes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(96), nullable=False)
    kcal_100g = Column(Float, nullable=False)
    fat = Column(Float, nullable=False)
    saturated_fat = Column(Float, nullable=False)
    carbohydrates = Column(Float, nullable=False)
    simple_sugars = Column(Float, nullable=False)
    fiber = Column(Float)
    proteins = Column(Float, nullable=False)
    salt = Column(Float, nullable=False)

class Recipes(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    recipe_id = Column(Integer, ForeignKey("dishes.id", ondelete="CASCADE"), unique=False, nullable=False)
    component_id = Column(Integer, ForeignKey("dishes.id", ondelete="CASCADE"), unique=False, nullable=False)
    amount = Column(Integer, nullable=False)

class DietEntry(Base):
    __tablename__ = "dietentry"
    id = Column(Integer, primary_key=True, autoincrement=True)
    added_at = Column(DateTime, default=func.now())
    entry_type = Column(String(20))
    food_id = Column(Integer, ForeignKey("dishes.id", ondelete="CASCADE"), unique=False)
    food_amount_in_grams = Column(Float)
    weight_in_kilograms = Column(Float)
    distance_in_kilometers = Column(Float)

class Events(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, autoincrement=True)
    event_at = Column(Date, default=func.now())
    organizer_name = Column(String(50))
    event_name = Column(String(50))
    kawanarajd = Column(Boolean)
    coffees_issued = Column(Integer)