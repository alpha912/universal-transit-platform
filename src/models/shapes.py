from sqlalchemy import Column, String, Float
from ..database import Base

class Shape(Base):
    __tablename__ = "shapes"

    shape_id = Column(String, primary_key=True)
    shape_pt_lat = Column(Float, nullable=False)
    shape_pt_lon = Column(Float, nullable=False)
    shape_pt_sequence = Column(Integer, nullable=False)
    shape_dist_traveled = Column(Float)
