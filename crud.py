from sqlalchemy.orm import Session

import models, schemas


def get_products(db: Session, skip: int = 0, limit: int = 100):
    today = '2022-08-21'
    test = db.query(models.RealPrice).join(models.Product).filter(models.RealPrice.date == today).order_by(models.RealPrice.variance)
    return test[:4], test[-4:]


def get_product(db: Session):
    return db.query(models.Product).first()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
