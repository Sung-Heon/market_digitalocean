from sqlalchemy.orm import Session

import models, schemas
from enum_type import CategoryType


def get_products(db: Session, category: CategoryType):
    today = '2022-08-21'
    if category:
        products = db.query(models.RealPrice, models.Product).join(models.Product,
                                                                   models.Product.id == models.RealPrice.product_id).filter(
            models.RealPrice.date == today, models.Product.category == category).order_by(
            models.RealPrice.variance).all()
    else:
        products = db.query(models.RealPrice, models.Product).join(models.Product,
                                                                   models.Product.id == models.RealPrice.product_id).filter(
            models.RealPrice.date == today).order_by(
            models.RealPrice.variance).all()
    return products[:4], products[-4:]


def get_product(db: Session):
    return db.query(models.Product).first()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
