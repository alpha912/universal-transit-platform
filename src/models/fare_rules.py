from sqlalchemy import Column, String, Integer
from ..database import Base

class FareRule(Base):
    __tablename__ = "fare_rules"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fare_id = Column(String)
    route_id = Column(String)
    origin_id = Column(String)
    destination_id = Column(String)
    contains_id = Column(String)
