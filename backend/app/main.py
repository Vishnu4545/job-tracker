from fastapi import FastAPI
from app.routes import job_routes

app = FastAPI()

app.include_router(job_routes.router)
