from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

import os
import sys

rpath = os.path.abspath('../../')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

from src.postgresql_table import create_tables
from src.postgrlsql_connection import create_database_engine

engine = create_database_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata = declarative_base().metadata

app = FastAPI()

class Message(BaseModel):
    msg_type: str
    msg_content: str
    sender_name: str
    msg_sent_time: float
    msg_dist_type: str
    time_thread_start: float
    reply_count: int
    reply_users_count: int

    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/messages/", response_model=list[Message])
def get_messages(db: Session = Depends(get_db)):
    message_table = create_tables(engine)
    messages = db.execute(select(message_table)).scalars().all()
    return messages