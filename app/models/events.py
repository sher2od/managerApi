from datetime import datetime
from sqlalchemy import Column,Integer,String,Text,DateTime,Enum,ForeignKey
from sqlalchemy.orm import relationship
import enum

from app.database import Base

class VenueTypes(str,enum.Enum):
    ONLINE = "online"
    OFFLINE = "ofline"
    HYBRID = "hybrid"

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(100),nullable=False)
    description = Column(Text,nullable=True)
    venue_type = Column(Enum(VenueTypes),nullable=False)
    location = Column(String(250),nullable=True)
    start_time = Column(DateTime,nullable=False)
    end_time = Column(DateTime,nullable=False)
    organizer_id = Column(Integer,ForeignKey("users.id"),nullable=False)

    created_at = Column(DateTime,default=datetime.utcnow,nullable=False)
    updated_at = Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)

    # relationship

    organizer = relationship("User",back_populates="events")
    
    