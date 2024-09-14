from sqlalchemy import Column, String, Integer
from ..database import Base

class CalendarDate(Base):
    __tablename__ = "calendar_dates"

    id = Column(Integer, primary_key=True, autoincrement=True)
    service_id = Column(String, index=True)
    date = Column(String)
    exception_type = Column(Integer)
