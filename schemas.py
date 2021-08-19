from pydantic import BaseModel


class ProductBase(BaseModel):
    sku: str
    name: str


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    sku: str
    name: str

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    name: str


class Category(CategoryBase):
    id: int
    name: str
    is_active: bool

    class Config:
        orm_mode = True
