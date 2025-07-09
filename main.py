from fastapi import FastAPI
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