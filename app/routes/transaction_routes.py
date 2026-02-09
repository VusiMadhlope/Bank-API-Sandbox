from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.schemas.transaction_schemas import TransactionCreate, TransactionResponse
from app.services.transaction_service import TransactionService

router = APIRouter(prefix="transactions", tags=["transactions"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/deposit/{account_id}")
def deposit(account_id: int, amount: float, db: Session = Depends(get_db)):
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")
    
    result = TransactionService.deposit(db=db, account_id=account_id, amount=amount)
    if result is None:
        raise HTTPException(status_code=404, detail="Account has not found")
    return {"message": f"Deposit ${amount} to account {account_id}, transaction: {result}"}

@router.post("/withdraw/{account_id}")
def withdraw(account_id: int, amount: float, db: Session = Depends(get_db)):
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be in the positive")
    
    result = TransactionService.withdraw(db=db, account_id=account_id, amount=amount)
    if result is None:
        raise HTTPException(status_code=404, detail="Account has not been found")
    elif isinstance(result, dict) and "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    
    return {"message": f"Withdraw ${amount} from account {account_id}, transaction: {result}"}

@router.post("/transfer/")
def transfer(from_account_id: int, to_account_id: int, amount: float, db:Session = Depends(get_db)):
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")
    
    result = TransactionService.transfer(
        db=db,
        from_account_id=from_account_id,
        to_account_id=to_account_id,
        amount=amount
    )

    if isinstance(result, dict) and "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return {"message": f"Transfer ${amount} from account {from_account_id} to account {to_account_id}, transaction: {result}"}