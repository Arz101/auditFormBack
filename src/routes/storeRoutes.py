from fastapi import APIRouter, Depends
from src.schemas import StoreCreate, StoreResponse, StoreUpdate
from src.config import get_db
from src.routes import get_current_user
from sqlalchemy.orm import Session
from src.controllers import StoreController

store = APIRouter()

store_controller = StoreController()

@store.post("/", response_model=StoreResponse, status_code=201)
def createStore(payload: StoreCreate, db: Session = Depends(get_db), _ = Depends(get_current_user)):
    return store_controller.create_Store(payload, db)

@store.get("/", response_model=list[StoreResponse], status_code=200)
def getStores(db: Session = Depends(get_db), _ = Depends(get_current_user)):
    return store_controller.getstores(db)

@store.put("/{id}", response_model=StoreResponse, status_code=201)
def updateStore(id: int, payload: StoreUpdate, db: Session = Depends(get_db), _ = Depends(get_current_user)):
    pass