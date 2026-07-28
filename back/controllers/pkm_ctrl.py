from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from main import get_db

pokemon_router = APIRouter(prefix="/pkm", tags=["Pokemon"])

@pokemon_router.post("/add")
async def add_pokemon(name: str, number: int, type1: str, type2: str = None, db: Session = Depends(get_db)):
    return {"Informações dos Pokémon atualizadas e adicionados"}

@pokemon_router.get("/get")
async def get_pokemon(name: str, number: int, db: Session = Depends(get_db)):
    return {"Informações do Pokémon retornadas com sucesso"}