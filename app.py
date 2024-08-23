from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from models import Ticket, TicketCreate, TicketResponse, SessionLocal


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React's default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# # Mock database
# tickets_db = [
#     {"name": "Alice", "email": "alice@example.com", "description": "Issue with logging in."},
#     {"name": "Bob", "email": "bob@example.com", "description": "Payment not processing."},
#     {"name": "Charlie", "email": "charlie@example.com", "description": "Account locked."}
# ]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/tickets", response_model=List[TicketResponse])
def get_tickets(db: Session = Depends(get_db)):
    tickets = db.query(Ticket).all()
    return tickets

@app.post("/tickets/", response_model=TicketResponse)
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    db_ticket = Ticket(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket