from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from main import get_db

cities_router = APIRouter(prefix="/cities", tags=["Cities"])

@cities_router.get("/get")
async def get_cities(db: Session = Depends(get_db)):
    
    raise HTTPException(status_code=200, detail="Lista de cidades retornada com sucesso")
    return {"message": "Lista de cidades retornada com sucesso"}
