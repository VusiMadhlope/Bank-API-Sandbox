from sqlalchemy import ForeignKey, Numeric
from sqlalchemy_venv import Column, Integer, String, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    account_number = Column(String(20), unique=True, index=True, nullable=False)
    account_type = Column(String(20), default="checking")
    balance = Column(Numeric(15, 2), default=0.00)
    currency = Column(String(20), default="ZAR")
    status = Column(String, default="active")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

# Relationships
user = relationship("User", back_populates="accounts")
transactions_sent = relationship("Transaction", foreign_keys='Transaction.from_account_id', back_populates="from_account")
transaction_received = relationship("Transaction", foreign_keys='Transaction.to_account_id', back_populates="to_account")

__table_args__ = (
    CheckConstraint('balance >= 0', name='non_negative_balance')
)
