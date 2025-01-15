from sqlalchemy import Column, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Raw(Base):
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
