from fastapi import FastAPI
from . import models, database
from .routes import category
from fastapi.middleware.cors import CORSMiddleware 

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(category.router, prefix="", tags=["Categorías"])

@app.get("/")
def read_root():
    return {"message": "Bienvenido al category_service"}
