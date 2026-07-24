# pyrefly: ignore [missing-import]
from fastapi import APIRouter, Depends
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session
from src.infra.database.database import get_db
from src.infra.database.entities.models import Route

router = APIRouter()

## ROUTES ===================================================

@router.post("/routes/add")
def add_route(region_id: int, route_number: int,pokeapi_name:str, lat: float, lng: float,
db: Session = Depends(get_db)):
    route = Route(region_id=region_id, route_number=route_number,pokeapi_name=pokeapi_name,
    lat=lat, lng=lng)
    db.add(route)
    db.commit()
    db.refresh(route)
    return route

@router.get("/routes")
def get_routes(db: Session = Depends(get_db)):
    routes = db.query(Route).all()
    return routes
