# pyrefly: ignore [missing-import]
from fastapi import FastAPI, Depends
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from models import Region, Route, City

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Pokemon SIG"}

@app.get("/regions")
def get_regions(db: Session = Depends(get_db)):
    regions = db.query(Region).all()
    return regions

@app.post("/regions/add")
def create_region(name: str, generation: int,  db: Session = Depends(get_db)):
    region = Region(name=name, generation=generation)
    db.add(region)
    db.commit()
    db.refresh(region)
    return region

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

def add_region(name:str,generation:int,db:Session = Depends(get_db)):    
    region = Region(name=name, generation=generation)
    db.add(region)
    db.commit()
    db.refresh(region)
    return region
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)