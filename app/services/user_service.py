from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCtreate
import hashlib

class UserService:
    @staticmethod
    def create_user(db: Session, user: UserCtreate):
        # Must hash the password in the application layer, user proper hashing like bcrypt
        hash_password = hashlib.sha256(user.password.encode()).hexdigest()
        db_user = User(
            name=user.name,
            email=user.email,
            hash_password=hash_password
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    @staticmethod
    def get_user(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def get_user_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()
