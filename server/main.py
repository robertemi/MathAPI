from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from config.config import init_db_pool
from routes.routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db_pool()
    yield

app = FastAPI(lifespan=lifespan)
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
app.include_router(router)
