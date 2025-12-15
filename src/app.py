from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from src.routes import *
from src.config import test_connection

def create_app():
    app = FastAPI() 

    if not test_connection():
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Database connection failed"
        )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],
    )   
    app.include_router(audit, prefix="/audits")
    app.include_router(auth, prefix="/auth")
    app.include_router(user, prefix="/users")
    app.include_router(store, prefix="/stores")
    app.include_router(quest, prefix="/questions")
    app.include_router(roles, prefix="/roles")
    app.include_router(sections, prefix="/sections")
    app.include_router(category, prefix="/categories")
    app.include_router(results, prefix="/results")

    return app