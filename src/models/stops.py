from sqlalchemy import Column, String, Float
from ..database import Base

class Stop(Base):
    __tablename__ = "stops"

    stop_id = Column(String, primary_key=True, index=True)
    stop_code = Column(String)
    stop_name = Column(String, nullable=False)
    stop_desc = Column(String)
    stop_lat = Column(Float, nullable=False)
    stop_lon = Column(Float, nullable=False)
    zone_id = Column(String)
    stop_url = Column(String)
    location_type = Column(String)
    parent_station = Column(String)
    stop_timezone = Column(String)
    wheelchair_boarding = Column(String)
    platform_code = Column(String)
