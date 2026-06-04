from sqlalchemy.orm import Session
from app.db import models

def get_categories(db: Session):
    """Retrieve all categories from the database"""
    return db.query(models.Category).all()

def create_category(db: Session, title: str):
    """Add a new book category row to the database"""
    db_category = models.Category(title=title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_books(db: Session):
    """Retrieve all books from the database"""
    return db.query(models.Book).all()

def create_book(db: Session, title: str, description: str, price: float, category_id: int, url: str = None):
    """Add a new book row connected to a category id"""
    db_book = models.Book(
        title=title, 
        description=description, 
        price=price, 
        category_id=category_id, 
        url=url
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
