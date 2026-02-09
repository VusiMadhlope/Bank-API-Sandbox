from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, JSON, CheckConstraint, func
from sqlalchemy.orm import relationship
from app.database import Base
import uuid

class Transaction(Base):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    transaction_reference = Column(String(50), unique=True, index=True, nullable=False, default=lambda: str(uuid.uuid4()))
    from_account_id = Column(Integer, ForeignKey("accounts.id"), nullable=True)  # Null for deposits
    to_account_id = Column(Integer, ForeignKey("accounts.id"), nullable=True)    # Null for withdrawals
    amount = Column(Numeric(15, 2), nullable=False)
    transaction_type = Column(String(20), nullable=False)  # deposit, withdrawal, transfer
    description = Column(String(255))
    status = Column(String(20), default="pending")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    metadata = Column(JSON)  # Store additional info

    # Relationships
    from_account = relationship("Account", foreign_keys=[from_account_id], back_populates="transactions_sent")
    to_account = relationship("Account", foreign_keys=[to_account_id], back_populates="transactions_received")
    
    __table_args__ = (
        CheckConstraint('amount > 0', name='positive_amount'),
    )