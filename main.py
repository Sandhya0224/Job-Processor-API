from fastapi import FastAPI
from models import init_db
from routers import jobs

app = FastAPI()
init_db()

app.include_router(jobs.router)
