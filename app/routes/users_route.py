from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.schemas.user_schemas import UserCreate, UserResponse
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])

#dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    #checking if user exists
    db_user = UserService.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email has already been registered")
    return UserService.create_user(db=db, user=user)

@router.get("/", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = UserService.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User has not been found")
    return db_user