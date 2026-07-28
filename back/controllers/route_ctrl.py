from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from main import get_db

route_router = APIRouter(prefix="/route", tags=["Route"])

@route_router.get("/get")
async def get_routes(db: Session = Depends(get_db)):
    return {"message": "Lista de rotas retornada com sucesso"}