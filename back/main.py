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
#from controllers.region_controllers import *
#from controllers.route_controllers import *
#from controller.city_controllers import *

app.include_router(pokemon_router)

if __name__ == "__main__":
    # pyrefly: ignore [missing-import]
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)