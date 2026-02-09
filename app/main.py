from fastapi import FastAPI
from app.routes import users_route, accounts_route, transaction_routes

app = FastAPI(
    title="Bank API Sandbox Project",
    description='A simulated banking system API for testing and development purposes.',
    version="1.0.0"
)

#include routers
app.include_router(users_route.router)
app.include_router(accounts_route.router)
app.include_router(transaction_routes.router)

@app.get("/")
def root():
    return {
        "message": "Welcome to the Bank API Sandbox",
        "docs": "/docs",
        "endpoints": {
            "users": "/users",
            "accounts": "/accounts",
            "transactions": "/transactions"
        } 
    }

#health check

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "Bank API Sandbox"}
