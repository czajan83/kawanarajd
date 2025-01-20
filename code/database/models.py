from sqlalchemy import Column, String, Float, ForeignKey, DateTime, func, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Raws(Base):
    __tablename__ = "raws"
    id = Column(String(32), primary_key=True)
    name = Column(String(96), nullable=False)
    kcal_100g = Column(Float, nullable=False)
    fat = Column(Float, nullable=False)
    saturated_fat = Column(Float, nullable=False)
    carbohydrates = Column(Float, nullable=False)
    simple_sugars = Column(Float, nullable=False)
    fiber = Column(Float)
    proteins = Column(Float, nullable=False)
    salt = Column(Float, nullable=False)
    cvi = Column(Float)

class Sauces(Base):
    __tablename__ = "sauces"
    id = Column(String(32), primary_key=True)
    name = Column(String(96), nullable=False)
    kcal_100g = Column(Float, nullable=False)
    fat = Column(Float, nullable=False)
    saturated_fat = Column(Float, nullable=False)
    carbohydrates = Column(Float, nullable=False)
    simple_sugars = Column(Float, nullable=False)
    fiber = Column(Float)
    proteins = Column(Float, nullable=False)
    salt = Column(Float, nullable=False)
    recipe = Column(String(500), nullable=False, default="onion:70, tomatoes:400")
    final_amount_in_grams = Column(Float, nullable=False)

class DietEntry(Base):
    __tablename__ = "dietentry"
    id = Column(String(32), primary_key=True)
    added_at = Column(String(24))
    entry_type = Column(String(20))
    food_id = Column(String(32))
    food_amount_in_grams = Column(Float)
    weight_in_kilograms = Column(Float)

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