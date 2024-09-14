from sqlalchemy import Column, String
from ..database import Base

class Agency(Base):
    __tablename__ = "agency"

    agency_id = Column(String, primary_key=True, index=True)
    agency_name = Column(String, nullable=False)
    agency_url = Column(String, nullable=False)
    agency_timezone = Column(String, nullable=False)
    agency_lang = Column(String)
    agency_phone = Column(String)
    agency_fare_url = Column(String)
    agency_email = Column(String)
