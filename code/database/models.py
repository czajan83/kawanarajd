from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

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
    ingr1_id = Column("ingr1_id", ForeignKey("raws.id", ondelete="CASCADE"), default = None, nullable=False)
    ingr1_amount = Column(Float, nullable=False)
    ingr2_id = Column("ingr2_id", ForeignKey("raws.id", ondelete="CASCADE"), default = None, nullable=False)
    ingr2_amount = Column(Float, nullable=False)
    ingr3_id = Column("ingr3_id", ForeignKey("raws.id", ondelete="CASCADE"), default = None)
    ingr3_amount = Column(Float)
    ingr4_id = Column("ingr4_id", ForeignKey("raws.id", ondelete="CASCADE"), default = None)
    ingr4_amount = Column(Float)
    final_weigh = Column(Float, nullable = False)
    raws = relationship("Raws", backref="raws")