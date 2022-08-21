# -*- coding: utf-8 -*-
"""
Main FastAPI app.
"""
# -*- coding: utf-8 -*-
from typing import List
import os

from fastapi import FastAPI, Query, Depends
from sqlalchemy.orm import Session

import crud
import schemas
from database import SessionLocal
from description import desc


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

@app.get("/test", response_model=List[schemas.Product])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tests = crud.get_products(db, skip=skip, limit=limit)
    return tests

@app.get("/test1", response_model=schemas.Product)
def read_user(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    test = crud.get_product(db)
    return test