from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from database import Base

from models import Location
from schemas import LocationCreate


Base.metadata.create_all(bind=engine)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



@app.get("/")
def home():

    return {
        "message":"Server running"
    }



@app.post("/save-location")
def save_location(
        data: LocationCreate,
        db: Session = Depends(get_db)
):

    location = Location(
        latitude=data.latitude,
        longitude=data.longitude
    )


    db.add(location)

    db.commit()

    db.refresh(location)


    return {
        "message":"Location saved",
        "id":location.id
    }

@app.get("/locations")
def get_locations(db: Session = Depends(get_db)):

    locations = db.query(Location).all()

    return locations

from sqlalchemy import text

@app.get("/check-db")
def check_db(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT current_database();"))
    return {
        "database": result.fetchone()[0]
    }