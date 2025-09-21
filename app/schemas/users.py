from pydantic import BaseModel,EmailStr,Field
from datetime import datetime

# umumiy sxema

class UserBase(BaseModel):
    username:str = Field(...,min_length=3,max_length=50)
    email:EmailStr
    full_name: str |None = Field(None,min_length=3,max_length=100)

# Yangi User yaratishda
class UserCreate(UserBase):
    password: str = Field(...,min_length=6)

# Userni yangilashda
class UserUpdate(BaseModel):
    username: str | None = Field(None, min_length=3, max_length=50)
    email: EmailStr | None = None
    full_name: str | None = Field(None, min_length=3, max_length=100)


# Userni qaytarishda
class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True