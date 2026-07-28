from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from main import get_db

route_router = APIRouter(prefix="/route", tags=["Route"])