from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from main import get_db

region_router = APIRouter(prefix="/region", tags=["Region"])

@region_router.get("/get")
async def get_regions(db: Session = Depends(get_db)):
    # Aqui você pode adicionar a lógica para buscar as regiões no banco de dados
    return {"message": "Lista de regiões retornada com sucesso"}