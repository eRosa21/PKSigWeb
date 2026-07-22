# pyrefly: ignore [missing-import]
from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from database import Base

class Region(Base):
    __tablename__ = "regions"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    generation = Column(Integer, nullable=False)
    description = Column(Text)

class Route(Base):
    __tablename__ = "routes"
    
    id = Column(Integer, primary_key=True, index=True)
    region_id = Column(Integer, ForeignKey("regions.id"), nullable=False)
    route_number = Column(Integer, nullable=False)
    #lat = Column(Float, nullable=True)
    #lng = Column(Float, nullable=True)

class City(Base):
    __tablename__ = "cities"
    
    id = Column(Integer, primary_key=True, index=True)
    region_id = Column(Integer, ForeignKey("regions.id"), nullable=False)
    name = Column(String(100), nullable=False)
    #lat = Column(Float, nullable=True)
    #lng = Column(Float, nullable=True)
    gym = Column(String(100))
    gym_type = Column(String(20))
    description = Column(Text)
'
class Pokemon(Base):
    __tablename__ = "pokemon"

    id = Column(Integer,primary_key=True)
    name = Column(String(50),unique= True, nullable=False)
    dex_number = Column(Integer,unique =True, nullable=False)
    type1 = Column(String(20), nullable=False)
    type2 = Column(String(20))
    weight = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)



