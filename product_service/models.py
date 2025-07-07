from sqlalchemy import Column, Integer, String, Float, ForeignKey
from .database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))  

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    info = Column(String(255))
    price = Column(Float, nullable=False)
    iva = Column(Float, nullable=False)
    image = Column(String(255))
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)