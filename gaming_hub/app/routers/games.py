from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
import time
from fastapi_cache.decorator import cache
from ..database import get_session
from ..models import Game, GameCreate

router = APIRouter(prefix="/games", tags=["Games"])

@router.post("/", response_model=Game)
def create_game(game: GameCreate, user_id: int, session: Session = Depends(get_session)):
    db_game = Game.model_validate(game, update={"user_id": user_id})
    session.add(db_game)
    session.commit()
    session.refresh(db_game)
    return db_game

# ENDPOINT AVANZADO: Simula una carga pesada y usa Redis para cachear la respuesta por 60 segundos
@router.get("/recommendations")
@cache(expire=60)
def get_recommendations():
    time.sleep(3) # Simulando una consulta pesada o un algoritmo de recomendación
    return {"recommendations": ["The Witcher 3", "Cyberpunk 2077", "Hollow Knight"]}

@router.delete("/{game_id}")
def delete_game(game_id: int, session: Session = Depends(get_session)):
    game = session.get(Game, game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Juego no encontrado")
    session.delete(game)
    session.commit()
    return {"ok": True}