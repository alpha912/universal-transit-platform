from sqlalchemy import Column, String, Boolean, Date
from ..database import Base

class Calendar(Base):
    __tablename__ = "calendar"

    service_id = Column(String, primary_key=True, index=True)
    monday = Column(Boolean)
    tuesday = Column(Boolean)
    wednesday = Column(Boolean)
    thursday = Column(Boolean)
    friday = Column(Boolean)
    saturday = Column(Boolean)
    sunday = Column(Boolean)
    start_date = Column(String)
    end_date = Column(String)
