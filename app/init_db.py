from app.db.db import engine, Base, SessionLocal
from app.db import crud, models

def init_database():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:
        existing_categories = crud.get_categories(db)
        if not existing_categories:
            print("Seeding initial data...")
            fiction = crud.create_category(db, title="Fiction")
            tech = crud.create_category(db, title="Technology")
            
            crud.create_book(db, title="The Great Gatsby", description="A classic novel", price=10.99, category_id=fiction.id)
            crud.create_book(db, title="1984", description="Dystopian fiction", price=12.50, category_id=fiction.id)
            
            crud.create_book(db, title="Python Crash Course", description="Learn Python fast", price=29.99, category_id=tech.id)
            crud.create_book(db, title="Clean Code", description="A handbook of agile software craftsmanship", price=35.00, category_id=tech.id)
            
            print("Database successfully initialized and seeded!")
        else:
            print("Database tables already exist and contain data.")
            
    finally:
        db.close()

if __name__ == "__main__":
    init_database()
