from app.db.db import SessionLocal
from app.db import crud

def display_data():
    db = SessionLocal()
    try:
        print("=== CATEGORIES ===")
        categories = crud.get_categories(db)
        for cat in categories:
            print(f"ID: {cat.id} | Title: {cat.title}")
            
        print("\n=== BOOKS IN DATABASE ===")
        books = crud.get_books(db)
        for book in books:
            print(f"[{book.category.title}] '{book.title}' - ${book.price:.2f} (Description: {book.description})")
            
    finally:
        db.close()

if __name__ == "__main__":
    display_data()
