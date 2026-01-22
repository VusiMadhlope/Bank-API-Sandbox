from sqlalchemy.orm import Session
from app.models.transactions import Transaction
from app.models.account import Account
from app.schemas.transaction import TransactionCreate
from datetime import datetime

class TransactionService:
    @staticmethod
    def deposit(db: Session, account_id: int, amount: float, description: str = None):
        """Handles deposit transactions into the account."""
        account = db.query(Account).filter(Account.id == account_id).first()
        if not account:
            return "Account does not exist"
        
        #Update account balance
        account.balance += amount

        #Create transaction records for deposit
        transaction = Transaction(
            to_account_id=account_id,
            amount=amount,
            transaction_type="withdrawal",
            description=description or f"Withdrawal of ${amount}",
            created_at=datetime.utcnow(),
            status="completed"
        )

        db.add(transaction)
        db.commit()
        db.refresh(transaction)
        return transaction
    
    @staticmethod
    def withdraw(db: Session, account_id: int, amount: float, description: str = None):
        """Handles the withdrawal transactions from the account."""

        account = db.query(Account).filter(Account.id == account_id).first()
        if not account:
            return "Account does not exist"
        
        #check if there's sufficient funds
        if account.balance < amount:
            return {"error": "Insufficient funds"}
        
        #Update balance
        account.balance -= amount

        #Create transaction record for withdrawal
        transaction = Transaction(
            to_account_id=account_id,
            amount=amount,
            transaction_type="withdrawal",
            description=description or f"Withdrawal of ${amount}",
            created_at=datetime.utcnow(),
            status="completed"
        )

        #transaction record for sender
        @staticmethod
        def transfer(db: Session, from_account_id: int, to_account_id: int, amount: float, description: str = None):
            """Handles transfer transactions between two accounts."""

            #check if accounts are different
            if from_account_id == to_account_id:
                return {"error": "Cannot transfer to the same account"}
            
            from_account_id = db.query(Account).filter(Account.id == from_account_id).first()

            to_account_id = db.query(Account).filter(Account.id == to_account_id).first()

            if not from_account_id or not to_account_id:
                return {"error": "One or both accounts do not exist"}
            
            #check if there's sufficient funds
            if from_account_id.balance < amount:
                return {"error": "Insufficient funds"}
            
            # Update balances (in a real app, this should be in a transaction)
            from_account_id.balance -= amount
            to_account_id.balance += amount

            #create tracnsaction record for transfer sender
             #Create transaction records
        transaction = Transaction(
            to_account_id=account_id,
            amount=amount,
            transaction_type="withdrawal",
            description=description or f"Transfer of ${amount}",
            created_at=datetime.utcnow(),
            status="completed"
        )

        db.add(transaction)
        db.commit()
        db.refresh(transaction)
        return transaction



