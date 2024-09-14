from .database import SessionLocal
from .services.ingestion_service import (
    ingest_agency,
    ingest_stops,
    ingest_routes,
    ingest_trips,
    ingest_calendar,
    ingest_calendar_dates,
    ingest_fare_attributes,
    ingest_fare_rules,
    ingest_feed_info,
    ingest_shapes,
)
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Starting GTFS data ingestion...")
    ingest_agency()
    ingest_stops()
    ingest_routes()
    ingest_trips()
    ingest_calendar()
    ingest_calendar_dates()
    ingest_fare_attributes()
    ingest_fare_rules()
    ingest_feed_info()
    ingest_shapes()
    logger.info("GTFS data ingestion completed.")
