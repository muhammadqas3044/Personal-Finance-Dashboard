from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend (served from file or http server) to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # safe for local dev; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Transaction(BaseModel):
    desc: str
    amount: float
    type: str  # "income" or "expense"

# in-memory store (temporary)
transactions: list[dict] = []

@app.get("/")
def home():
    return {"message": "Welcome to Personal Finance API!"}

@app.get("/transactions")
def get_transactions():
    return transactions

@app.post("/transactions")
def add_transaction(t: Transaction):
    transactions.append(t.dict())
    return {"message": "Transaction added", "transactions": transactions}

@app.delete("/transactions/{index}")
def delete_transaction(index: int):
    if 0 <= index < len(transactions):
        transactions.pop(index)
        return {"message": "Transaction deleted", "transactions": transactions}
    return {"error": "Transaction not found"}
