from dotenv import load_dotenv
load_dotenv("../.env")

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import init_db
from .routes.user_routes import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # initialize db
    await init_db()
    yield
    
    # add future shutdown logic here

app = FastAPI(lifespan=lifespan)
app.include_router(user_router)

origins = ["http://127.0.0.1:5173", "http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
