from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from main import get_db

cities_router = APIRouter(prefix="/cities", tags=["Cities"])