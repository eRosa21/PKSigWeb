# pyrefly: ignore [missing-import]
from fastapi import APIRouter, Depends, HTTPException
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session
import requests
from src.infra.database.database import get_db

router = APIRouter()

## POKEMON ===================================================

@router.get("/pokemon/{pokemon_identifier}")
def get_pokemon_locations(pokemon_identifier: str,db: Session = Depends(get_db)):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_identifier.lower()}/encounters"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        raise HTTPException(status_code=404,detail ="Pokemon não encontrado ou erro na API")

    info = resposta.json()
    location_names = [item['location_area']['name'] for item in info]

    return {"pokemon": pokemon_identifier, "pokeapi_locations": location_names}
