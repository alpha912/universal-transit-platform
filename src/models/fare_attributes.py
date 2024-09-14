from sqlalchemy import Column, String, Float, Integer
from ..database import Base

class FareAttribute(Base):
    __tablename__ = "fare_attributes"

    fare_id = Column(String, primary_key=True)
    price = Column(Float, nullable=False)
    currency_type = Column(String, nullable=False)
    payment_method = Column(Integer)
    transfers = Column(Integer)
    transfer_duration = Column(Integer)
