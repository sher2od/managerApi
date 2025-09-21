
from .database import SessionalLocal

def get_db():
    db = SessionalLocal()
    try:
        yield db
    finally:
        db.close()