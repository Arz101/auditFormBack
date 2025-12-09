# src/database/init_db.py
from src.models import *
#from src.models.base import Base
from .db import engine

def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
