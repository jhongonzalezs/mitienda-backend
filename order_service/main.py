from fastapi import FastAPI
from .database import Base, engine
from .models import OrderItem
from .routes import order 
from fastapi.middleware.cors import CORSMiddleware 

Base.metadata.create_all(bind=engine, tables=[OrderItem.__table__])

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(order.router, prefix="", tags=["Ordenes"])

@app.get("/")
def read_root():
    return {"message": "Bienvenido al order_service"}
