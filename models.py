from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref

from database import Base



class RealPrice(Base):
    __tablename__ = "real_price"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Integer)
    date = Column(String)
    variance = Column(Integer)

    product_id = Column(Integer,ForeignKey('product.id'))


class PredictPrice(Base):
    __tablename__ = "predict_price"

    id = Column(Integer, primary_key=True, index=True)
    predict_price = Column(Integer)
    date = Column(String)
    variance = Column(Integer)

    product_id = Column(Integer,ForeignKey('product.id'))


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    picture_url = Column(String)
    description = Column(String)
    name = Column(String)
    selling = Column(Boolean)
    category = Column(String)

