# Tutorial de Consumo de APIs con Python

Este proyecto contiene ejemplos prácticos para aprender a consumir APIs REST utilizando la biblioteca `requests` de Python. Cada archivo incluye un ejemplo independiente y comentado para facilitar el estudio, la práctica y la reutilización del código.

---

## Requisitos

- Python 3.7 o superior
- Biblioteca `requests` (puedes instalarla con `pip install requests`)

---

## Estructura del Proyecto

## 📚 Descripción de los Archivos

### `01_get_request.py`

Realiza una solicitud `GET` a `http://httpbin.org/get` y guarda el contenido HTML recibido en un archivo. Imprime el contenido en consola si la respuesta es exitosa.

### `02_get_with_params.py`

Envía parámetros en la URL utilizando el argumento `params` de `requests.get`. Muestra cómo enviar datos como parte de la URL.

### `03_post_request.py`

Ejecuta una solicitud `POST` vacía a `http://httpbin.org/post` y muestra la respuesta que devuelve el servidor. Útil para ver cómo responde el servidor ante solicitudes sin datos.

### `04_post_with_json.py`

Envía un diccionario de datos como `JSON` en una solicitud `POST`. Luego analiza la respuesta como `JSON` y extrae información relevante como la IP del cliente (`origin`).

---

## ✨ Objetivo

Este conjunto de ejemplos busca enseñarte cómo:

Hacer solicitudes `GET` y `POST`

- Enviar parámetros y cuerpos JSON

- Manejar respuestas y errores

- Ver datos devueltos por una API de prueba

---


