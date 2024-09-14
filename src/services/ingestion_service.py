import pandas as pd
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models.agency import Agency
from ..models.stops import Stop
from ..models.routes import Route
from ..models.trips import Trip
from ..models.calendar import Calendar
from ..models.calendar_dates import CalendarDate
from ..models.fare_attributes import FareAttribute
from ..models.fare_rules import FareRule
from ..models.feed_info import FeedInfo
from ..models.shapes import Shape
import os
import logging

logger = logging.getLogger(__name__)

gtfs_path = os.path.join(os.getcwd(), 'data', 'gtfs')

def ingest_agency():
    db = SessionLocal()
    agency_file = os.path.join(gtfs_path, 'agency.txt')
    agency_df = pd.read_csv(agency_file)

    for _, row in agency_df.iterrows():
        agency = Agency(
            agency_id=row['agency_id'],
            agency_name=row['agency_name'],
            agency_url=row['agency_url'],
            agency_timezone=row['agency_timezone'],
            agency_lang=row.get('agency_lang'),
            agency_phone=row.get('agency_phone'),
            agency_fare_url=row.get('agency_fare_url'),
            agency_email=row.get('agency_email')
        )
        db.merge(agency)
    db.commit()
    db.close()
    logger.info("Agency data ingested successfully.")

def ingest_stops():
    db = SessionLocal()
    stops_file = os.path.join(gtfs_path, 'stops.txt')
    stops_df = pd.read_csv(stops_file)

    for _, row in stops_df.iterrows():
        stop = Stop(
            stop_id=row['stop_id'],
            stop_code=row.get('stop_code'),
            stop_name=row['stop_name'],
            stop_desc=row.get('stop_desc'),
            stop_lat=row['stop_lat'],
            stop_lon=row['stop_lon'],
            zone_id=row.get('zone_id'),
            stop_url=row.get('stop_url'),
            location_type=row.get('location_type'),
            parent_station=row.get('parent_station'),
            stop_timezone=row.get('stop_timezone'),
            wheelchair_boarding=row.get('wheelchair_boarding'),
            platform_code=row.get('platform_code')
        )
        db.merge(stop)
    db.commit()
    db.close()
    logger.info("Stops data ingested successfully.")

def ingest_routes():
    db = SessionLocal()
    routes_file = os.path.join(gtfs_path, 'routes.txt')
    routes_df = pd.read_csv(routes_file)

    for _, row in routes_df.iterrows():
        route = Route(
            route_id=row['route_id'],
            agency_id=row.get('agency_id'),
            route_short_name=row['route_short_name'],
            route_long_name=row['route_long_name'],
            route_desc=row.get('route_desc'),
            route_type=row['route_type'],
            route_url=row.get('route_url'),
            route_color=row.get('route_color'),
            route_text_color=row.get('route_text_color')
        )
        db.merge(route)
    db.commit()
    db.close()
    logger.info("Routes data ingested successfully.")

def ingest_trips():
    db = SessionLocal()
    trips_file = os.path.join(gtfs_path, 'trips.txt')
    trips_df = pd.read_csv(trips_file)

    for _, row in trips_df.iterrows():
        trip = Trip(
            trip_id=row['trip_id'],
            route_id=row['route_id'],
            service_id=row['service_id'],
            trip_headsign=row.get('trip_headsign'),
            trip_short_name=row.get('trip_short_name'),
            direction_id=row.get('direction_id'),
            block_id=row.get('block_id'),
            shape_id=row.get('shape_id'),
            wheelchair_accessible=row.get('wheelchair_accessible'),
            bikes_allowed=row.get('bikes_allowed')
        )
        db.merge(trip)
    db.commit()
    db.close()
    logger.info("Trips data ingested successfully.")

def ingest_calendar():
    db = SessionLocal()
    calendar_file = os.path.join(gtfs_path, 'calendar.txt')
    calendar_df = pd.read_csv(calendar_file)

    for _, row in calendar_df.iterrows():
        calendar = Calendar(
            service_id=row['service_id'],
            monday=bool(row['monday']),
            tuesday=bool(row['tuesday']),
            wednesday=bool(row['wednesday']),
            thursday=bool(row['thursday']),
            friday=bool(row['friday']),
            saturday=bool(row['saturday']),
            sunday=bool(row['sunday']),
            start_date=row['start_date'],
            end_date=row['end_date']
        )
        db.merge(calendar)
    db.commit()
    db.close()
    logger.info("Calendar data ingested successfully.")

def ingest_calendar_dates():
    db = SessionLocal()
    calendar_dates_file = os.path.join(gtfs_path, 'calendar_dates.txt')
    calendar_dates_df = pd.read_csv(calendar_dates_file)

    for _, row in calendar_dates_df.iterrows():
        calendar_date = CalendarDate(
            service_id=row['service_id'],
            date=row['date'],
            exception_type=row['exception_type']
        )
        db.add(calendar_date)
    db.commit()
    db.close()
    logger.info("Calendar Dates data ingested successfully.")

def ingest_fare_attributes():
    db = SessionLocal()
    fare_attributes_file = os.path.join(gtfs_path, 'fare_attributes.txt')
    fare_attributes_df = pd.read_csv(fare_attributes_file)

    for _, row in fare_attributes_df.iterrows():
        fare_attribute = FareAttribute(
            fare_id=row['fare_id'],
            price=row['price'],
            currency_type=row['currency_type'],
            payment_method=row.get('payment_method'),
            transfers=row.get('transfers'),
            transfer_duration=row.get('transfer_duration')
        )
        db.merge(fare_attribute)
    db.commit()
    db.close()
    logger.info("Fare Attributes data ingested successfully.")

def ingest_fare_rules():
    db = SessionLocal()
    fare_rules_file = os.path.join(gtfs_path, 'fare_rules.txt')
    fare_rules_df = pd.read_csv(fare_rules_file)

    for _, row in fare_rules_df.iterrows():
        fare_rule = FareRule(
            fare_id=row['fare_id'],
            route_id=row.get('route_id'),
            origin_id=row.get('origin_id'),
            destination_id=row.get('destination_id'),
            contains_id=row.get('contains_id')
        )
        db.add(fare_rule)
    db.commit()
    db.close()
    logger.info("Fare Rules data ingested successfully.")

def ingest_feed_info():
    db = SessionLocal()
    feed_info_file = os.path.join(gtfs_path, 'feed_info.txt')
    feed_info_df = pd.read_csv(feed_info_file)

    for _, row in feed_info_df.iterrows():
        feed_info = FeedInfo(
            feed_publisher_name=row['feed_publisher_name'],
            feed_publisher_url=row['feed_publisher_url'],
            feed_lang=row['feed_lang'],
            feed_start_date=row.get('feed_start_date'),
            feed_end_date=row.get('feed_end_date'),
            feed_version=row.get('feed_version'),
            feed_contact_email=row.get('feed_contact_email'),
            feed_contact_url=row.get('feed_contact_url')
        )
        db.merge(feed_info)
    db.commit()
    db.close()
    logger.info("Feed Info data ingested successfully.")

def ingest_shapes():
    db = SessionLocal()
    shapes_file = os.path.join(gtfs_path, 'shapes.txt')
    shapes_df = pd.read_csv(shapes_file)

    for _, row in shapes_df.iterrows():
        shape = Shape(
            shape_id=row['shape_id'],
            shape_pt_lat=row['shape_pt_lat'],
            shape_pt_lon=row['shape_pt_lon'],
            shape_pt_sequence=row['shape_pt_sequence'],
            shape_dist_traveled=row.get('shape_dist_traveled')
        )
        db.add(shape)
    db.commit()
    db.close()
    logger.info("Shapes data ingested successfully.")
