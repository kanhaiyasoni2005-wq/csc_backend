
from fastapi import FastAPI
from app.routers.application import application_route
from app.core.db import Base
from app.core.db import engine
from fastapi.middleware.cors import CORSMiddleware
from app.routers.user import user_routes
from app.routers.service import service_routes
from app.routers.category import category_routes
from app.routers.payment import payment_router
Base.metadata.create_all(bind = engine)

app = FastAPI(
    title="Application API",
    description="API for managing applications, documents and images",
    version="1.0.0"
)
app.add_middleware(
       CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],

)

# Register application routes
app.include_router(application_route)
app.include_router(user_routes)
app.include_router(service_routes)
app.include_router(category_routes)
app.include_router(payment_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Application API",
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
