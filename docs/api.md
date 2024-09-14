# API Documentation

Welcome to the Universal Transit Platform API documentation. This guide provides detailed information about all available API endpoints.

---

## Table of Contents

- [Introduction](#introduction)
- [Endpoints](#endpoints)
  - [Health Check](#health-check)
  - [Agencies](#agencies)
  - [Stops](#stops)
  - [Fare Calculation](#fare-calculation)
- [Authentication](#authentication)
- [Error Handling](#error-handling)
- [Examples](#examples)
- [Contact](#contact)

---

## Introduction

The Universal Transit Platform API allows you to access public transportation data, including agencies, stops, routes, and fare information. It is designed to be easy to use and integrate into your applications.

**Base URL**:

```
http://localhost:8000
```

---

## Endpoints

### Health Check

- **Endpoint**: `/health`
- **Method**: `GET`
- **Description**: Check the status of the API.
- **Response**:

  ```json
  {
    "status": "ok"
  }
  ```

### Agencies

- **Endpoint**: `/agencies`
- **Method**: `GET`
- **Description**: Retrieve a list of transit agencies.
- **Parameters**:
  - `skip` (integer, optional): Number of records to skip for pagination.
  - `limit` (integer, optional): Maximum number of records to return.
- **Response**:

  ```json
  [
    {
      "agency_id": "agency_id",
      "agency_name": "Agency Name",
      "agency_url": "http://www.agencyurl.com",
      "agency_timezone": "Timezone",
      "agency_lang": "en",
      "agency_phone": "123-456-7890",
      "agency_fare_url": "http://www.agencyurl.com/fares",
      "agency_email": "info@agencyurl.com"
    },
    ...
  ]
  ```

### Stops

- **Endpoint**: `/stops`
- **Method**: `GET`
- **Description**: Retrieve a list of transit stops.
- **Parameters**:
  - `skip` (integer, optional): Number of records to skip for pagination.
  - `limit` (integer, optional): Maximum number of records to return.
- **Response**:

  ```json
  [
    {
      "stop_id": "stop_id",
      "stop_name": "Stop Name",
      "stop_lat": 12.345678,
      "stop_lon": -98.765432,
      "stop_desc": "Description of the stop",
      "zone_id": "zone_id",
      "stop_url": "http://www.stopurl.com",
      "location_type": "0",
      "parent_station": "parent_stop_id",
      "stop_timezone": "Timezone",
      "wheelchair_boarding": "1",
      "platform_code": "Platform 1"
    },
    ...
  ]
  ```

### Fare Calculation

- **Endpoint**: `/fare/{route_id}`
- **Method**: `GET`
- **Description**: Calculate the fare for a specific route.
- **Parameters**:
  - `route_id` (string, required): The ID of the route for which to calculate the fare.
- **Response**:

  ```json
  {
    "fare_id": "fare_id",
    "price": 2.50,
    "currency": "USD"
  }
  ```

  If no fare is found:

  ```json
  {
    "message": "Fare not found for the given route"
  }
  ```

---

## Authentication

Currently, the API does not require authentication. All endpoints are publicly accessible. Future versions may include API keys or OAuth authentication.

---

## Error Handling

The API uses standard HTTP status codes to indicate the success or failure of an API request.

- **200 OK**: The request was successful.
- **400 Bad Request**: The request was invalid or cannot be served.
- **404 Not Found**: The requested resource could not be found.
- **500 Internal Server Error**: An error occurred on the server.

---

## Examples

### Get Health Status

**Request**:

```bash
curl http://localhost:8000/health
```

**Response**:

```json
{
  "status": "ok"
}
```

### Retrieve Agencies

**Request**:

```bash
curl http://localhost:8000/agencies?skip=0&limit=10
```

**Response**:

```json
[
  {
    "agency_id": "1",
    "agency_name": "City Transit Agency",
    "agency_url": "http://www.citytransitagency.com",
    "agency_timezone": "America/New_York",
    "agency_lang": "en",
    "agency_phone": "555-1234",
    "agency_fare_url": "http://www.citytransitagency.com/fares",
    "agency_email": "info@citytransitagency.com"
  },
  // More agencies...
]
```

### Calculate Fare for a Route

**Request**:

```bash
curl http://localhost:8000/fare/10
```

**Response**:

```json
{
  "fare_id": "fare_10",
  "price": 3.00,
  "currency": "USD"
}
```

---

## Contact

If you have any questions or need further assistance, please open an [issue on GitHub](https://github.com/yourusername/universal-transit-platform/issues) or contact us at [universaltransitplatform@gmail.com](mailto:universaltransitplatform@gmail.com).

---

**Note**:

- Replace `localhost` with your server's address if running on a different host.
- Ensure that the API is running before making requests.
- Update the examples with actual data from your database.
- Replace `yourusername` with your actual GitHub username.