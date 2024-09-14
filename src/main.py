from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import engine, Base, SessionLocal
from .models.agency import Agency
from .models.stops import Stop
from .services.fare_service import calculate_fare

# Import all models to ensure they are registered properly on the metadata
from .models import agency, stops, routes, trips, calendar, calendar_dates, fare_attributes, fare_rules, feed_info, shapes

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Universal Transit Platform API",
    description="An API to unify global public transportation data and services.",
    version="0.1.0",
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/agencies")
def read_agencies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    agencies = db.query(Agency).offset(skip).limit(limit).all()
    return agencies

@app.get("/stops")
def read_stops(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stops = db.query(Stop).offset(skip).limit(limit).all()
    return stops

@app.get("/fare/{route_id}")
def get_fare(route_id: str, db: Session = Depends(get_db)):
    fare = calculate_fare(db, route_id)
    if fare:
        return {
            "fare_id": fare.fare_id,
            "price": fare.price,
            "currency": fare.currency_type
        }
    else:
        return {"message": "Fare not found for the given route"}
