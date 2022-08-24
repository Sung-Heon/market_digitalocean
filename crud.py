from sqlalchemy.orm import Session
from sqlalchemy import or_
import models, schemas
from enum_type import CategoryType


def get_products(db: Session, category: CategoryType):
    today = '2022-08-21'
    if category:
        products = db.query(models.RealPrice, models.Product, models.PredictPrice).join(models.RealPrice).join(
            models.PredictPrice).filter(
            models.RealPrice.date == today, models.Product.category == category).order_by(
            models.RealPrice.variance).all()
    else:
        products = db.query(models.RealPrice, models.Product).join(models.RealPrice).join(
            models.PredictPrice).filter(
            models.RealPrice.date == today).order_by(
            models.RealPrice.variance).all()
    decreased_product = products[:4]
    increasing_product = sorted(products, key=lambda i: i['PredictPrice'].variance, reverse=True)[:4]
    return decreased_product, increasing_product


def get_product(db: Session):
    return db.query(models.Product).first()


def get_product_detail(product_id: int, db: Session):
    today = '2022-08-21'
    one_week_before = '2022-08-14'
    two_week_before = '2022-08-07'

    return db.query(models.RealPrice.price, models.RealPrice.date,models.RealPrice.product_id,models.Product).join(models.Product).filter(or_(
        models.RealPrice.date == today, models.RealPrice.date == one_week_before,
        models.RealPrice.date == two_week_before), models.RealPrice.product_id==product_id).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
