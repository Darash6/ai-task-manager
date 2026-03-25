from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.routes import router

app = FastAPI(title="AI Task Manager API")

Base.metadata.create_all(bind=engine)

app.include_router(router)