from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from . import models, database
from .routes import product

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product.router, prefix="", tags=["Productos"])

@app.get("/")
def read_root():
    return {"message": "Bienvenido al product_service"}
