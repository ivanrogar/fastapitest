from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from database import Base

catalog_category_association_table = Table('catalog_product_categories', Base.metadata,
                          Column('product_id', ForeignKey('catalog_product.id')),
                          Column('category_id', ForeignKey('catalog_category.id'))
                          )


class Product(Base):
    __tablename__ = "catalog_product"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String(255), unique=True)
    name = Column(String(255))
    categories = relationship("Category", secondary=catalog_category_association_table)


class Category(Base):
    __tablename__ = "catalog_category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    is_active = Column(Boolean, default=True)

