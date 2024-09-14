from sqlalchemy import Column, String
from ..database import Base

class FeedInfo(Base):
    __tablename__ = "feed_info"

    feed_publisher_name = Column(String, nullable=False)
    feed_publisher_url = Column(String, nullable=False)
    feed_lang = Column(String, nullable=False)
    feed_start_date = Column(String)
    feed_end_date = Column(String)
    feed_version = Column(String)
    feed_contact_email = Column(String)
    feed_contact_url = Column(String)
