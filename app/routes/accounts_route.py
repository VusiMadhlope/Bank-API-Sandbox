from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.schemas.account_schemas import AccountCreate, AccountResponse
from app.services.account_service import AccountService

router = APIRouter(prefix="/accounts", tags=["accounts"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AccountResponse)
def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    db_account = AccountService.create_account(db=db, account=account)
    if not db_account:
        raise HTTPException(status_code=400, detail="Account creation has failed")
    return db_account

@router.get("/{account_id}", response_model=AccountResponse)
def get_account(account_id: int, db: Session = Depends(get_db)):
    db_account = AccountService.get_account(db=db, account_id=account_id)
    if not db_account:
        raise HTTPException(status_code=404, detail="Account has not been found")
    return db_account