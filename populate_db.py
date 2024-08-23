# populate_db.py
from models import SessionLocal, Ticket

db = SessionLocal()

db.add_all([
    Ticket(name="Alice", email="alice@example.com", description="Issue with logging in."),
    Ticket(name="Bob", email="bob@example.com", description="Payment not processing."),
    Ticket(name="Charlie", email="charlie@example.com", description="Account locked.")
])

db.commit()
db.close()
