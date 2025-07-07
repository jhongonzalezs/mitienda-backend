from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Guardar producto
@router.post("/products", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Listar Productos
@router.get("/products", response_model=list[schemas.Product])
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()

# Buscar Productos por id
@router.get("/products/{product_id}", response_model=schemas.Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product

# Actualizar Productos por id
@router.put("/products/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, updated: schemas.ProductCreate, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    for key, value in updated.dict().items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)
    return product

# Eliminar Productos por id
@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(product)
    db.commit()
    return {"message": "Producto eliminado correctamente"}


# Obtener productos por categoría
@router.get("/categories/{category_id}/products", response_model=list[schemas.Product])
def get_products_by_category(category_id: int, db: Session = Depends(get_db)):
    products = db.query(models.Product).filter(models.Product.category_id == category_id).all()
    return products

# Subir producto con imagen (archivo real)
@router.post("/products/upload")
async def create_product_with_image(
    name: str = Form(...),
    description: str = Form(...),
    info: str = Form(...),
    price: float = Form(...),
    iva: float = Form(...),
    image: UploadFile = File(...),
    category_id: int = Form(None),
    db: Session = Depends(get_db)
):
    # Guardar la imagen en disco local
    contents = await image.read()
    path = f"uploads/{image.filename}"

    with open(path, "wb") as f:
        f.write(contents)

    # Crear producto con ruta de imagen
    new_product = models.Product(
        name=name,
        description=description,
        info=info,
        price=price,
        iva=iva,
        image=path,  
        category_id=category_id
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product