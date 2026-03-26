from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.routes import router

app = FastAPI(title="AI Task Manager API")

Base.metadata.create_all(bind=engine)

#"use http://localhost:8000/docs to access the API documentation"
#"use docker-compose up to start the application"


app.include_router(router)
