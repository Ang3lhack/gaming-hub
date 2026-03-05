import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from .database import create_db_and_tables
from .routers import users, games, uploads

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 1. Crear las tablas de la base de datos al iniciar
    create_db_and_tables()
    
    # 2. Configurar la URL de Redis de forma segura
    # Render inyectará tu enlace de Upstash aquí. Si no lo encuentra, usa el local.
    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
    
    # Iniciar conexión con Redis para el caché
    redis = aioredis.from_url(redis_url, encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    
    yield
    # Limpieza al apagar la app (opcional)

app = FastAPI(title="Gaming Hub API", lifespan=lifespan)

# Servir archivos estáticos (imágenes de avatares)
# Asegúrate de que la carpeta app/static/uploads exista
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Incluir los routers (rutas)
app.include_router(users.router)
app.include_router(games.router)
app.include_router(uploads.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a Gaming Hub API 🚀"}