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

- cd nombre_del_servicio
- python -m venv venv
- source venv/bin/activate (linux)
- pip install -r requirements.txt
- cd ..

# Abre 5 terminales y ejecuta lo siguiente en cada una:
## auth
- cd auth_service
- source venv/bin/activate
- cd ..
- uvicorn auth_service.main:app --reload --port 8001

## cart
- cd cart_service
- source venv/bin/activate
- cd ..
- uvicorn cart_service.main:app --reload --port 8002

## category
- cd category_service
- source venv/bin/activate
- cd ..
- uvicorn category_service.main:app --reload --port 8003

## order
- cd order_service
- source venv/bin/activate
- cd ..
- uvicorn order_service.main:app --reload --port 8004

## product
- cd product_service
- source venv/bin/activate
- cd ..
- uvicorn product_service.main:app --reload --port 8005



# forma correcta de ejecutar las pruebas con pytest


- cd nombre_del_servicio
- source venv/bin/activate
- cd ..
- python -m pytest nombre_del_servicio/tests

## ejemplo: 

- cd auth_service
- source venv/bin/activate
- cd ..
- python -m pytest auth_service/tests








## 📄 Caso de Uso: Registrar Pedido

**ID:** CU-005  
**Nombre del caso de uso:** Registrar Pedido (Orden de Compra)  
**Actor principal:** Usuario  
**Descripción:**  
El usuario realiza una compra desde el frontend seleccionando productos previamente agregados en su carrito. El sistema registra estos productos como un nuevo pedido mediante el microservicio `order_service`.

---

### ✅ Precondiciones

- El usuario debe haber iniciado sesión (`auth_service`).
- El usuario debe tener productos agregados al carrito (`cart_service`).
- Los productos deben existir en el sistema (`product_service`).

---

### 🔁 Flujo Principal

| Paso | Actor   | Acción |
|------|---------|--------|
| 1    | Usuario | Inicia sesión en la plataforma (`POST /users/login`) |
| 2    | Usuario | Agrega productos al carrito (`POST /cart`) |
| 3    | Usuario | Confirma la compra desde el carrito |
| 4    | Sistema | Recupera los productos del carrito del usuario |
| 5    | Sistema | Envía los productos como `OrderItemCreate[]` a `POST /orders` |
| 6    | Sistema | Registra el pedido en la tabla `order_items` |
| 7    | Sistema | Devuelve mensaje de éxito y los datos del pedido registrado |

---

### ❗️Flujos Alternativos

- **Producto no existente**: Si el `product_id` no existe, el sistema responde con `404 Producto no encontrado`.
- **Cantidad inválida**: Si `quantity <= 0`, se responde con un error `400`.

---

### ✅ Postcondiciones

- El pedido queda almacenado en la base de datos en la tabla `order_items`.
- El usuario puede consultar sus pedidos usando:
  - `GET /orders` para ver todos los pedidos
  - `GET /orders/{order_id}` para ver los detalles de uno

---

### 🧱 Tablas Relacionadas

- **order_items**
```sql
id INT PRIMARY KEY AUTO_INCREMENT,
order_id INT,
product_id INT,
quantity INT,
unit_price FLOAT
