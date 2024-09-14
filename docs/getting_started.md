# Getting Started

Welcome to the Universal Transit Platform! This guide will help you set up the project on your local machine for development and testing purposes.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Navigate to the Project Directory](#2-navigate-to-the-project-directory)
  - [3. Create and Activate a Virtual Environment](#3-create-and-activate-a-virtual-environment)
  - [4. Install Dependencies](#4-install-dependencies)
  - [5. Set Up the Database](#5-set-up-the-database)
  - [6. Run the Data Ingestion Script](#6-run-the-data-ingestion-script)
  - [7. Run the Application](#7-run-the-application)
  - [8. Access the API Documentation](#8-access-the-api-documentation)
- [Troubleshooting](#troubleshooting)
- [Next Steps](#next-steps)

---

## Prerequisites

Ensure you have the following installed on your system:

- **Python 3.8** or higher
- **Git**
- **Virtual environment** tools (`venv` is included with Python 3.8+)
- **SQLite** (comes pre-installed with Python)

---

## Installation

### 1. Clone the Repository

Open your terminal or command prompt and run:

```bash
git clone https://github.com/yourusername/universal-transit-platform.git
```

Replace `yourusername` with your GitHub username if you have forked the repository.

### 2. Navigate to the Project Directory

```bash
cd universal-transit-platform
```

### 3. Create and Activate a Virtual Environment

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Set Up the Database

For development purposes, we'll use SQLite. No additional setup is required; the database will be created automatically.

### 6. Run the Data Ingestion Script

Download and extract a GTFS dataset into the `data/gtfs` directory.

**Note**: Ensure that the `data/gtfs` directory contains the GTFS `.txt` files (e.g., `agency.txt`, `stops.txt`).

Run the ingestion script:

```bash
python -m src.ingest_gtfs
```

### 7. Run the Application

Start the FastAPI application using Uvicorn:

```bash
uvicorn src.main:app --reload
```

### 8. Access the API Documentation

Open your web browser and navigate to:

```
http://127.0.0.1:8000/docs
```

You should see the interactive Swagger UI with all the available API endpoints.

---

## Troubleshooting

- **Module Not Found Error**:

  Ensure you're running the script from the project root directory and using the `-m` flag for module execution.

- **Virtual Environment Activation Issues**:

  Verify that your virtual environment is activated. The command prompt should show `(venv)` at the beginning.

- **Dependency Installation Errors**:

  If you encounter errors during `pip install`, try upgrading `pip`:

  ```bash
  pip install --upgrade pip
  ```

- **Database Errors**:

  Ensure that the data ingestion script ran successfully and that the `transit.db` file exists in the project root.

---

## Next Steps

- **Explore the API**: Use the Swagger UI to test the API endpoints.
- **Contribute**: Check out the [Contributing Guidelines](../CONTRIBUTING.md) to see how you can help improve the project.
- **Implement Features**: Pick an open issue or suggest a new feature.

---

**If you encounter any issues or have questions, please open an [issue on GitHub](https://github.com/yourusername/universal-transit-platform/issues).**

---

**Note**:

- Replace `yourusername` with your actual GitHub username.
- Ensure you have the necessary GTFS data files in the `data/gtfs` directory before running the ingestion script.
- All code blocks are properly formatted for easy copying.