from fastapi import FastAPI
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String

DATABASE_URL = 'sqlite:///./test.db'
app = FastAPI()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)

Base.metadata.create_all(bind=engine)

@app.post('/notes')
def create_note(title, content):
    db = SessionLocal()
    note = Note(title=title, content=content)
    db.add(note)
    db.commit()
    db.refresh(note)
    db.close()
    return note

@app.get('/notes')
def list_notes():
    db = SessionLocal()
    notes = db.query(Note).all()
    db.close()
    return notes