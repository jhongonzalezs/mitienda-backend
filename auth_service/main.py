from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, database
from .routes import user 

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


origins = [
    "http://localhost:5173",  
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluye rutas
app.include_router(user.router)

# Ruta raíz
@app.get("/")
def read_root():
    return {"message": "Bienvenido al auth_service"}
