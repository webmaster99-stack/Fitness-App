from fastapi import FastAPI, status
from api import register_routes
from database.core import Base, engine
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(engine)
    yield


app = FastAPI(
    debug=True,
    title="Calorie Tracker API",
    version="0.1.0",
    lifespan=lifespan
)


register_routes(app)


@app.get("/", status_code=status.HTTP_200_OK)
def welcome():
    return {
        "message": "Welcome to the Calorie Tracker API",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "healthy"}
