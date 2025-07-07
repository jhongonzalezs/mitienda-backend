from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/users", tags=["Usuarios"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Obtener todos los usuarios
@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

# Crear usuario
@router.post("/")
def create_user(data: schemas.UserCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == data.username).first()
    if user:
        raise HTTPException(status_code=400, detail="Usuario ya existe")
    new_user = models.User(username=data.username, password=data.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"id": new_user.id, "username": new_user.username}

# Iniciar sesión
@router.post("/login")
def login(data: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == data.username).first()
    if not user or user.password != data.password:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    
    return {
        "id": user.id,
        "username": user.username,
        "message": f"Bienvenido, {user.username}"
    }