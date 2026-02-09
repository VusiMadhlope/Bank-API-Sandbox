from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class AccountCreate(BaseModel):
    user_id: int
    account_type: str
    initial_balance: float
    currency: str

class AccountResponse(BaseModel):
    id: int
    account_number: str
    account_type: str
    balance: float
    currency: str
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True