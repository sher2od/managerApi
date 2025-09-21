from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app import models,schemas


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# Yangi user yaratish
@router.post("/",response_model=schemas.UserOut,status_code=status.HTTP_201_CREATED)
def create_user(user:schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Barcha userlarni olish
@router.get("/",response_model=list[schemas.UserOut])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

# Bitta user olish
@router.get("/{user_id}",response_model=schemas.UserOut)
def get_user(user_id:int,db:Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User topilmadi")
    return db_user


#Userni yangilash
@router.put("/{user_id}",response_model=schemas.UserOut)
def update_user(user_id:int,update_data: schemas.UserUpdate,db:Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        for key, value in update_data.dict(exclude_unset=True).items():
            setattr(db_user, key, value)

        db.commit()
        db.refresh(db_user)
        return db_user

# Userni o'chirish
@router.delete("/{user_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id:int,db:Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:raise HTTPException(status_code=404, detail="User topilmadi")
    
    db.delete(db_user)
    db.commit()
    return {"detail": "User o‘chirildi"}