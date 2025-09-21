from datetime import datetime
from sqlalchemy import Column,Integer,String,DateTime,Enum
from sqlalchemy.orm import relationship
import enum

from app.database import Base

class UserTypes(str,enum.Enum):
    ADMIN = "admin"
    ORGANIZER = "organizer"
    USER = "user"

class User(Base):
    __tableame__ = "users"

    id = Column(Integer,nullable=True,index=True)
    username = Column(String(50),unique=True,nullable=False,index=True)
    email = Column(String(100),unique=True,nullable=False,index=True)
    full_name = Column(String(100),nullable=False)
    user_type = Column(Enum(UserTypes),nullable=False)

    created_at = Column(DateTime,default=datetime.utcnow,nullable=False)
    updated_at = Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)

    # relationship 
    events = relationship("Event",back_populates="organizer")