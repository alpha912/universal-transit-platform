import pytest
from sqlalchemy.orm import Session
from src.database import SessionLocal
from src.services.fare_service import calculate_fare

def test_calculate_fare():
    db = SessionLocal()
    # Use a valid route_id from your data
    route_id = "1"  
    fare = calculate_fare(db, route_id)
    assert fare is not None
    assert fare.price > 0
    db.close()
