from fastapi import FastAPI
from .database import Base, engine
from .models import OrderItem
from .routes import order 

Base.metadata.create_all(bind=engine, tables=[OrderItem.__table__])

app = FastAPI()
app.include_router(order.router, prefix="", tags=["Ordenes"])

@app.get("/")
def read_root():
    return {"message": "Bienvenido al order_service"}
