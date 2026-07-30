import os 
from fastapi import FastAPI, Depends, HTTPException
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from src.infra.database.database import engine, Base, get_db
from src.infra.entities.models import Region, Route, City, Pokemon
import requests

Base.metadata.create_all(bind=engine)

app = FastAPI()
    
from controllers.pkm_ctrl import pokemon_router
from controllers.region_ctrl import region_router
from controllers.route_ctrl import route_router
from controllers.city_ctrl import cities_router

app.include_router(pokemon_router)
app.include_router(region_router)
app.include_router(route_router)
app.include_router(cities_router)

if __name__ == "__main__":
    # pyrefly: ignore [missing-import]
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)