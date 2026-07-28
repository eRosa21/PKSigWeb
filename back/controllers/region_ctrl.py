from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from main import get_db

region_router = APIRouter(prefix="/region", tags=["Region"])