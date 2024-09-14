from sqlalchemy import Column, String
from ..database import Base

class Trip(Base):
    __tablename__ = "trips"

    trip_id = Column(String, primary_key=True, index=True)
    route_id = Column(String, nullable=False)
    service_id = Column(String, nullable=False)
    trip_headsign = Column(String)
    trip_short_name = Column(String)
    direction_id = Column(String)
    block_id = Column(String)
    shape_id = Column(String)
    wheelchair_accessible = Column(String)
    bikes_allowed = Column(String)
