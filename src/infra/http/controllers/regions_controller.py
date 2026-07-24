# pyrefly: ignore [missing-import]
from fastapi import APIRouter, Depends, HTTPException
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session
from src.infra.database.database import get_db
from src.infra.database.entities.models import Region

router = APIRouter()

## Regions ===================================================

@router.get("/regions")
def get_regions(db: Session = Depends(get_db)):
    regions = db.query(Region).all()
    return regions

@router.post("/region/add")
def add_region(name:str,generation:int,db:Session = Depends(get_db)):
    region = Region(name=name, generation=generation)
    db.add(region)
    db.commit()
    db.refresh(region)
    return region

@router.put("/regions/update")
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

@router.delete("/regions/delete")
def delete_region(region_id:int, db:Session = Depends(get_db)):
    region = db.query(Region).filter(Region.id == region_id).first()

    if not region:
        raise HTTPException(status_code=404, detail="Região não encontrada")

    db.delete(region)
    db.commit()
    return {"Message": f"A Região {region.name} deletada com sucesso"}
