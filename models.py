# models.py
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./tickets.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# SQLAlchemy model
class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    description = Column(String)

Base.metadata.create_all(bind=engine)

# Pydantic models
class TicketBase(BaseModel):
    name: str
    email: str
    description: str

class TicketCreate(TicketBase):
    pass

class TicketResponse(TicketBase):
    id: int

    class Config:
        orm_mode = True
