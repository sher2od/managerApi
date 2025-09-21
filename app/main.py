from fastapi import FastAPI
from .database import engine, Base
from . import models  # bu app/__init__.py orqali models chaqirilyapti
from .routers import users, events

# Jadval yaratish
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Meneger Event")

# Routerni ulash
app.include_router(users.router)
app.include_router(events.router)
