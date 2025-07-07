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


# Agregar producto al carrito
@router.post("/cart", response_model=schemas.CartItem)
def add_to_cart(item: schemas.CartItemCreate, db: Session = Depends(get_db)):
    db_item = models.CartItem(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# Listar carrito
@router.get("/cart/{user_id}", response_model=list[schemas.CartItem])
def get_user_cart(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.CartItem).filter(models.CartItem.user_id == user_id).all()


# Editar cantidad
@router.put("/cart/{item_id}", response_model=schemas.CartItem)
def update_quantity(item_id: int, item: schemas.CartItemUpdate, db: Session = Depends(get_db)):
    cart_item = db.query(models.CartItem).filter(models.CartItem.id == item_id).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    cart_item.quantity = item.quantity
    db.commit()
    db.refresh(cart_item)
    return cart_item


# Eliminar item
@router.delete("/cart/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    cart_item = db.query(models.CartItem).filter(models.CartItem.id == item_id).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    db.delete(cart_item)
    db.commit()
    return {"message": "Item eliminado del carrito"}
