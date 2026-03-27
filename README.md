## Bank API Sandbox

By defitiniton A Bank API Sandbox is a simulated banking system that mimics how real financial instiutions manage accounts, balances and transactions. It is a safe testing environment that behaves as a real bank without the need for real money.

## Overview
By mimicing a real bank API, this project allows us to establish the following:
- 👤 Create virtual customers who hold bank accounts
- 💳 Create virtual bank accounts with unique account numbers
- 💰 Perform bank operations (deposits, withdrawals, transfers)
- 📊 Track all transactions with a complete audit trail
- 🔒 Test banking logic without real money

## Features
- **User Management** - Create and manage bank customers
- **Account Management** - Create accounts with unique account numbers
- **Deposit Operations** - Add money to accounts
- **Withdrawal Operations** - Remove money with insufficient funds protection
- **Transfer Operations** - Move money between accounts
- **Transaction Ledger** - Complete audit trail of all operations
- **PostgreSQL Database** - Robust data persistence
- **RESTful API** - Well-documented endpoints via FastAPI

- ## Tech Stack
### Backend
- **Python 3.13** - Core programming language
- **FastAPI** - Modern web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **PostgreSQL** - Production-ready relational database
- **Pydantic** - Data validation and settings management

- ## Architecture

The project follows a clean 3-layer architecture:

1. **Models Layer** (`app/models/`) - Defines database table structures
2. **Services Layer** (`app/services/`) - Contains business logic and rules
3. **Routes Layer** (`app/routes/`) - Handles HTTP requests/responses

Create and activate virtual environment
# Windows
python -m venv sqlalchemy_venv
sqlalchemy_venv\Scripts\activate

# Mac/Linux
python -m venv sqlalchemy_venv
source sqlalchemy_venv/bin/activate
