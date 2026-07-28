from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from main import get_db

pokemon_router = APIRouter(prefix="/pkm", tags=["Pokemon"])

@pokemon_router.get("/add")
async def add_pokemon(name: str, type1: str, type2: str = None, db: Session = Depends(get_db)):
    return {"Conectado"}