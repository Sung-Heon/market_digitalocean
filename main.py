# -*- coding: utf-8 -*-
"""
Main FastAPI app.
"""
# -*- coding: utf-8 -*-
from typing import List, Optional
import os

from fastapi import FastAPI, Query, Depends
from sqlalchemy.orm import Session

import crud
import schemas
from database import SessionLocal
from description import desc
from enum_type import CategoryType

app = FastAPI(
    title="Something Random...",
    description=desc,
    version="0.0.1",
    docs_url="/",
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/products/{category}')
def get_products(category: Optional[CategoryType], db: Session = Depends(get_db)):
    products_rise_top4, products_decrease_top4 = crud.get_products(db, category=category)
    return products_rise_top4, products_decrease_top4


@app.get('/products')
def get_products(db: Session = Depends(get_db)):
    products_rise_top4, products_decrease_top4 = crud.get_products(db, category=None)
    return products_rise_top4, products_decrease_top4


@app.get('/product/{product_id}')
def get_product_detail(product_id: int, db: Session = Depends(get_db)):
    product_detail = crud.get_product_detail(product_id=product_id, db=db)
    print(product_detail)
    return product_detail


@app.get("/test1", response_model=schemas.Product)
def read_user(db: Session = Depends(get_db)):
    test = crud.get_product(db)
    return test
