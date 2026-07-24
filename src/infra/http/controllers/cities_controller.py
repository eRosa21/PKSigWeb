# pyrefly: ignore [missing-import]
from fastapi import APIRouter, Depends
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session
from src.infra.database.database import get_db
from src.infra.database.entities.models import City

router = APIRouter()

## CITIES ===================================================

@router.post("/cities/add")
def add_city(region_id: int, name: str,pokeapi_name:str, lat: float, lng: float,
description: str, gym: str, gym_type:str,db: Session = Depends(get_db)):
    city = City(region_id=region_id, name=name,pokeapi_name=pokeapi_name,
    lng = lng, lat = lat, description = description, gym = gym, gym_type = gym_type)
    db.add(city)
    db.commit()
    db.refresh(city)
    return city

@router.get("/cities")
def get_cities(db: Session = Depends(get_db)):
    cities = db.query(City).all()
    return cities
