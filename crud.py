from sqlalchemy.orm import Session

import models
import schemas


def get_product(db: Session, sku: str):
    return db.query(models.Product).filter(models.Product.sku == sku).first()


def get_product_by_id(db: Session, id: int):
    return db.query(models.Product).filter(models.Product.id == id).first()


def get_products(db: Session, skip: int = 0, limit: int = 12):
    return db.query(models.Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: schemas.ProductCreate):
    new_product = models.Product(sku=product.sku, name=product.name)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

