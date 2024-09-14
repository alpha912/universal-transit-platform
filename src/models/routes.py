from sqlalchemy import Column, String
from ..database import Base

class Route(Base):
    __tablename__ = "routes"

    route_id = Column(String, primary_key=True, index=True)
    agency_id = Column(String)
    route_short_name = Column(String, nullable=False)
    route_long_name = Column(String, nullable=False)
    route_desc = Column(String)
    route_type = Column(String, nullable=False)
    route_url = Column(String)
    route_color = Column(String)
    route_text_color = Column(String)
