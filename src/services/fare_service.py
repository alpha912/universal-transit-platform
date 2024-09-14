from sqlalchemy.orm import Session
from ..models.fare_attributes import FareAttribute
from ..models.fare_rules import FareRule

def calculate_fare(db: Session, route_id: str):
    # Simplified fare calculation based on route_id
    fare_rules = db.query(FareRule).filter(FareRule.route_id == route_id).all()
    if not fare_rules:
        return None
    fare_ids = {rule.fare_id for rule in fare_rules}
    fares = db.query(FareAttribute).filter(FareAttribute.fare_id.in_(fare_ids)).all()
    # Return the lowest fare as an example
    if fares:
        return min(fares, key=lambda x: x.price)
    return None
