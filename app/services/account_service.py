from random import random
import string
from sqlalchemy.orm import Session
from app.models.account import Account
from app.models.user import User
from app.schemas.account import AccountCreate

class AccountService:
    @staticmethod
    def generate_account_number():
        '''Generates a unique account number. In a real-world scenario, this should ensure uniqueness across the database.'''
        bank_code = "BANK"
        random_digits = "".join(random.choices(string.digits, k=10))
        return f"{bank_code}-{random_digits}"
    
    @staticmethod
    def create_account(db: Session, account: AccountCreate):
        #check if user exists
        user = db.query(User).filter(User.id == account.user_id).first()
        if not user:
            return "User does not exist"
        
        db_account = Account(
            user_id=account.user_id,
            account_number=AccountService.generate_account_number(),
            account_type=account.account_type,
            balance=account.initial_balance,
            currency=account.currency
        )

        db.add(db_account)
        db.commit()
        db.refresh(db_account)
        return db_account
    
    @staticmethod
    def get_account(db: Session, account_number: str):
        return db.query(Account).filter(Account.account_number == account_number).first()