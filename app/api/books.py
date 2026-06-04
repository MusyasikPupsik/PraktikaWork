from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.db import get_db
from app.db import crud
from app import schemas

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=List[schemas.BookResponse])
def list_books(category_id: Optional[int] = Query(None), db: Session = Depends(get_db)):
    return crud.get_books(db, category_id=category_id)

@router.get("/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_id(db, book_id=book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.post("/", response_model=schemas.BookResponse, status_code=status.HTTP_201_CREATED)
def create_new_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    if not crud.get_category_by_id(db, book.category_id):
        raise HTTPException(status_code=400, detail="Category does not exist")
    return crud.create_book(db, title=book.title, description=book.description, price=book.price, category_id=book.category_id, url=book.url)

@router.put("/{book_id}", response_model=schemas.BookResponse)
def edit_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    if not crud.get_category_by_id(db, book.category_id):
        raise HTTPException(status_code=400, detail="Category does not exist")
    db_book = crud.update_book(db, book_id=book_id, title=book.title, description=book.description, price=book.price, category_id=book.category_id, url=book.url)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_book(book_id: int, db: Session = Depends(get_db)):
    success = crud.delete_book(db, book_id=book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
