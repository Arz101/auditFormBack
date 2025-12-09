from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import audit, auth, user, store


def create_app():
    app = FastAPI() 
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],
    )   
    app.include_router(audit, prefix="/audit")
    app.include_router(auth, prefix="/auth")
    app.include_router(user, prefix="/user")
    app.include_router(store, prefix="/store")

    return app