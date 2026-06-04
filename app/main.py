from fastapi import FastAPI
from app.api import books, categories
from app.db.db import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Octagon Book API")

app.include_router(categories.router)
app.include_router(books.router)

@app.get("/health")
def health_check():
    return {"status": "healthy"}
