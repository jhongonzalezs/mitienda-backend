# 🛒 MiTienda Backend

Repositorio del backend de **MiTienda**, una aplicación web de ventas desarrollada como prueba técnica para Develop App.

Esta solución está construida con **Python**, **FastAPI**, **SQLAlchemy**, **MySQL** y una **arquitectura de microservicios**.

---

## 📦 Estructura de Microservicios

- `auth_service`: Registro e inicio de sesión de usuarios
- `cart_service`: Gestión del carrito de compras
- `category_service`: Administración de categorías de productos
- `product_service`: CRUD de productos
- `order_service`: Registro de pedidos

---

## 🔧 Requisitos

Antes de empezar, asegúrate de tener lo siguiente instalado:

- Python 3.10+
- MySQL o Docker con MySQL
- Git
- Uvicorn (`pip install uvicorn`)
- MySQL Workbench (opcional)

---

## 🚀 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/jhongonzalezs/mitienda-backend.git
cd mitienda-backend

```

# Repite en cada carpeta: auth_service, cart_service, category_service, product_service, order_service

cd nombre_del_servicio
python -m venv venv
source venv/bin/activate (linux)
pip install -r requirements.txt
cd ..

# Abre 5 terminales y ejecuta lo siguiente en cada una:

cd auth_service
source venv/bin/activate
cd ..
uvicorn auth_service.main:app --reload --port 8001

cd cart_service
source venv/bin/activate
cd ..
uvicorn cart_service.main:app --reload --port 8002

cd category_service
source venv/bin/activate
cd ..
uvicorn category_service.main:app --reload --port 8003

cd order_service
source venv/bin/activate
cd ..
uvicorn order_service.main:app --reload --port 8004

cd product_service
source venv/bin/activate
cd ..
uvicorn product_service.main:app --reload --port 8005



# forma correcta de ejecutar las pruebas con pytest


cd nombre_del_servicio
source venv/bin/activate
cd ..
python -m pytest nombre_del_servicio/tests

cd auth_service
source venv/bin/activate
cd ..
python -m pytest auth_service/tests
