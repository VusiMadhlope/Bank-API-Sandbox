from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class TransactionCreate(BaseModel):
    from_account_id: Optional[int]
    to_account_id: Optional[int]
    amount: float
    transaction_type: str
    description: Optional[str] = None

class TransactionResponse(BaseModel):
    id: int
    transaction_reference: str
    from_account_id: Optional[int]
    to_account_id: Optional[int]
    amount: float
    transaction_type: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True