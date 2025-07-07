from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Crear pedido
@router.post("/orders", response_model=list[schemas.OrderItem])
def create_order(items: list[schemas.OrderItemCreate], db: Session = Depends(get_db)):
    order_items = []
    for item in items:
        db_item = models.OrderItem(**item.dict())
        db.add(db_item)
        order_items.append(db_item)
    db.commit()
    return order_items

# Listar todos los pedidos
@router.get("/orders", response_model=list[schemas.OrderItem])
def get_all_orders(db: Session = Depends(get_db)):
    return db.query(models.OrderItem).all()


# Ver pedido por order_id
@router.get("/orders/{order_id}", response_model=list[schemas.OrderItem])
def get_order_by_id(order_id: int, db: Session = Depends(get_db)):
    items = db.query(models.OrderItem).filter(models.OrderItem.order_id == order_id).all()
    if not items:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return items
