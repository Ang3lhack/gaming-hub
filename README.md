# 🚀 Gaming Hub API

Una API RESTful de nivel profesional desarrollada con FastAPI para gestionar usuarios y sus bibliotecas de videojuegos. 

Este proyecto demuestra la implementación de una arquitectura organizada, validación de datos robusta, persistencia en base de datos relacional y el uso de caché en memoria para optimizar respuestas pesadas.

## 📖 Descripción del Dominio del Proyecto
**Gaming Hub** permite a los usuarios registrarse en la plataforma (con su propia foto de perfil) y gestionar una colección de sus videojuegos favoritos. El sistema ofrece funcionalidades de CRUD completo para usuarios y juegos, relacionándolos mediante llaves foráneas. Además, simula un motor de recomendaciones de juegos utilizando caché avanzado para respuestas instantáneas.

## 🛠️ Tecnologías Utilizadas
* **Framework Web:** FastAPI
* **ORM y Base de Datos:** SQLModel + SQLite (Local)
* **Caché en Memoria:** Redis (Upstash en producción)
* **Validación de Datos:** Pydantic (con JSON Schema avanzado)
* **Servidor ASGI:** Uvicorn
* **Despliegue:** Render.com

---

## 💻 Instrucciones de Instalación Local (Windows)

### 1. Preparar el entorno
Abre tu terminal (PowerShell), clona el proyecto y entra a la carpeta principal:
```powershell
# Entrar a la carpeta del proyecto
cd gaming_hub

# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
.\venv\Scripts\Activate.ps1
