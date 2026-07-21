# pyrefly: ignore [missing-import]
from fastapi import FastAPI, Depends, HTTPException
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from models import Region, Route, City
import requests

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/regions")
def get_regions(db: Session = Depends(get_db)):
    regions = db.query(Region).all()
    return regions

#@app.post("/regions/create")
#def create_region(name: str, generation: int,  db: Session = Depends(get_db)):
 #   region = Region(name=name, generation=generation)
  #  db.add(region)
   # db.commit()
    #db.refresh(region)
    #return region

@app.post("/region/add")
def add_region(name:str,generation:int,db:Session = Depends(get_db)):    
    region = Region(name=name, generation=generation)
    db.add(region)
    db.commit()
    db.refresh(region)
    return region

@app.put("/regions/update")
def update_region(region_id:int, name:str,generation:int,db:Session = Depends(get_db)):
    region = db.query(Region).filter(Region.id == region_id).first()
    
    if not region:
        
        raise
    HTTPException(status_code=404,detail ="Região não encontrada")
    region.name = name
    region.generation=generation
    
    db.commit()
    db.refresh(region)
    return region

@app.delete("/regions/delete")
def delete_region(region_id:int, name:str, generation:int, db:Session = Depends(get_db)):
    region = db.query(Region).filter(Region.id == region_id).first()
    
    if not region:
        raise HTTPException(status_code=404, detail="Região não encontrada")
    
    db.delete(region)
    db.commit()
    return {"Message": f"A Região {region.name} deletada com sucesso"}

@app.post("/routes/add")
def add_route(region_id: int, route_number: int, 
#lat: float, lng: float, 
db: Session = Depends(get_db)):
    route = Route(region_id=region_id, route_number=route_number,
    # lat=lat, lng=lng
    )
    db.add(route)
    db.commit()
    db.refresh(route)
    return route

@app.get("/routes")
def get_routes(db: Session = Depends(get_db)):
    routes = db.query(Route).all()
    return routes

@app.post("/cities/add")
def add_city(region_id: int, name: str,
#lat: float, lng: float,
description: str, gym: str, gym_type:str,db: Session = Depends(get_db)):
    city = City(region_id=region_id, name=name,
    #lng = lng, lat = lat,
    description = description, gym = gym, gym_type = gym_type)
    db.add(city)
    db.commit()
    db.refresh(city)
    return city

@app.get("/cities")
def get_cities(db: Session = Depends(get_db)):
    cities = db.query(City).all()
    return cities

@app.get("/pokemon/{pokemon_identifier}")
def get_pokemon_locations(pokemon_identifier: str):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_identifier.lower()}/encounters"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        info = resposta.json()
        locations = [item['location_area']['name'] for item in info]
        return locations
    else:
        return []

pokemon_name = "turtwig"
pokemon_id = "387"
pokemon_info = get_pokemon_locations(pokemon_id or pokemon_name)

if pokemon_info:
    print(f"Localizações da espécie {pokemon_name}:")
    for loc in pokemon_info:
        print(f'- {loc}')
else:
    print(f"Não foi possivel encontrar informações de {pokemon_name}")

if __name__ == "__main__":
    # pyrefly: ignore [missing-import]
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)