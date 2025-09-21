from pydantic import BaseModel,Field
from datetime import datetime

#Umumiy sxema
class EventBase(BaseModel):
    title: str = Field(...,min_length=3,max_length=100)
    description: str | None = Field(None,max_length=250)
    location: str | None = Field(None,max_length=150)
    start_time:datetime
    end_time: datetime

# Yangi event yaratishda
class EventCreate(EventBase):
    organizer_id:int 

# Eventni yangilashda
class EventUpdate(BaseModel):
    title: str | None = Field(None, min_length=3, max_length=100)
    description: str | None = Field(None, max_length=250)
    location: str | None = Field(None, max_length=150)
    start_time: datetime | None = None
    end_time: datetime | None = None

# Qaytarishda
class EventOut(EventBase):
    id: int
    organizer_id: int
    created_at: datetime
    updated_at: datetime | None

    class Config:
        from_attributes = True