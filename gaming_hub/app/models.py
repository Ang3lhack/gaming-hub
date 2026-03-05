from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel
from pydantic import ConfigDict

class GameBase(SQLModel):
    title: str = Field(index=True, min_length=2, max_length=100)
    genre: str = Field(index=True)
    tags: str = Field(default="") # Separados por comas

class Game(GameBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    owner: Optional["User"] = Relationship(back_populates="games")

class GameCreate(GameBase):
    pass

class UserBase(SQLModel):
    username: str = Field(index=True, unique=True, min_length=3)
    email: str = Field(unique=True)
    avatar_url: Optional[str] = Field(default=None)

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    games: List[Game] = Relationship(back_populates="owner")

class UserCreate(UserBase):
    # Ejemplo de JSON Schema extra para la documentación
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "username": "GamerPro99",
                "email": "gamer@example.com"
            }
        }
    )