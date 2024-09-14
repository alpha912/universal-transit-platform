# Data Ingestion Guide

This guide provides instructions on how to ingest GTFS (General Transit Feed Specification) data into the Universal Transit Platform.

---

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [GTFS Data Structure](#gtfs-data-structure)
- [Steps to Ingest Data](#steps-to-ingest-data)
  - [1. Obtain GTFS Data](#1-obtain-gtfs-data)
  - [2. Prepare the Data Directory](#2-prepare-the-data-directory)
  - [3. Run the Ingestion Script](#3-run-the-ingestion-script)
  - [4. Verify the Ingestion](#4-verify-the-ingestion)
- [Troubleshooting](#troubleshooting)
- [Frequently Asked Questions](#frequently-asked-questions)
- [Contact](#contact)

---

## Introduction

GTFS is a standard format for public transportation schedules and associated geographic information. By ingesting GTFS data, we populate the database with up-to-date transit information.

---

## Prerequisites

- Ensure that the project is set up according to the [Getting Started Guide](getting_started.md).
- The virtual environment is activated.
- Dependencies are installed (`pip install -r requirements.txt`).

---

## GTFS Data Structure

GTFS data typically comes as a ZIP file containing several text files, such as:

- `agency.txt`
- `stops.txt`
- `routes.txt`
- `trips.txt`
- `stop_times.txt`
- `calendar.txt`
- `calendar_dates.txt`
- `fare_attributes.txt`
- `fare_rules.txt`
- `shapes.txt`
- `feed_info.txt`

---

## Steps to Ingest Data

### 1. Obtain GTFS Data

- **Option 1**: Download GTFS data from transit agencies' websites.
- **Option 2**: Use repositories like [TransitFeeds](https://transitfeeds.com/) to find GTFS data.

### 2. Prepare the Data Directory

- Create a directory named `gtfs` inside the `data` folder if it doesn't exist:

  ```bash
  mkdir -p data/gtfs
  ```

- Extract the contents of the GTFS ZIP file into the `data/gtfs` directory. Ensure that all the `.txt` files are directly inside `data/gtfs`.

### 3. Run the Ingestion Script

From the project root directory, run:

```bash
python -m src.ingest_gtfs
```

- This script will read the GTFS files and populate the database accordingly.
- It may take a few minutes depending on the size of the GTFS data.

### 4. Verify the Ingestion

- Check that the `transit.db` file has been created or updated.
- Use the API endpoints to retrieve data and ensure it's correctly loaded.

For example, run the application:

```bash
uvicorn src.main:app --reload
```

Then navigate to `http://localhost:8000/agencies` to see if agency data is available.

---

## Troubleshooting

- **File Not Found Error**: Ensure that the GTFS `.txt` files are correctly placed in the `data/gtfs` directory.
- **Database Errors**: Delete the existing `transit.db` file and rerun the ingestion script to start fresh.
- **Import Errors**: Make sure you're running the script with the `-m` flag and from the project root directory.

---

## Frequently Asked Questions

### **Q**: Can I ingest data from multiple transit agencies?

**A**: Yes, you can. Place each agency's GTFS data in separate folders within `data/gtfs` and modify the ingestion script to process multiple directories.

### **Q**: How often should I update the GTFS data?

**A**: It's recommended to update the data whenever a new GTFS feed is released by the transit agency, usually every few months.

### **Q**: What if the GTFS data has additional files not listed here?

**A**: The ingestion script may need to be updated to handle additional GTFS files or fields.

---

## Contact

If you encounter issues or have questions not covered in this guide, please:

- Open an [issue on GitHub](https://github.com/yourusername/universal-transit-platform/issues).
- Contact us at [universaltransitplatform@gmail.com](mailto:universaltransitplatform@gmail.com).

---

**Note**:

- Replace `yourusername` with your actual GitHub username.
- Ensure that you have the necessary permissions to use the GTFS data from the transit agency.
- Be aware of any licensing or data usage restrictions.