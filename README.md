KPA Forms API Backend
This project is a backend service developed as part of an API development assignment. It implements two key API endpoints from the KPA-ERP specification using Python, FastAPI, and PostgreSQL to handle the submission and retrieval of wheel specification forms.

Table of Contents
Technologies & Tech Stack

Project Structure

Implemented APIs

Create Wheel Specification

Get Wheel Specifications

Setup and Installation

Running the Server

Limitations and Assumptions

Technologies & Tech Stack
The project was built using a modern and robust tech stack:

Backend Framework: FastAPI for high-performance, asynchronous API development.

Database: PostgreSQL, a powerful open-source relational database. The project is configured to connect to a cloud-hosted instance (e.g., Supabase).

Database ORM: SQLAlchemy for elegant and Pythonic database interactions.

Data Validation: Pydantic for robust data validation, serialization, and settings management.

Web Server: Uvicorn, a lightning-fast ASGI server.

Database Driver: psycopg2-binary to connect the application to the PostgreSQL database.

Project Structure
The project follows a logical and scalable structure to separate concerns:

kpa_backend/
├── app/
│   ├── __init__.py
│   ├── main.py         # Main FastAPI app, defines API endpoints and middleware.
│   ├── schemas.py      # Pydantic schemas for request/response data validation.
│   ├── models.py       # SQLAlchemy ORM models for database tables.
│   ├── crud.py         # Reusable functions for database operations (Create, Read).
│   └── database.py     # Database connection and session management.
├── venv/               # Python virtual environment folder.
└── requirements.txt    # List of project dependencies.

Implemented APIs
Two API endpoints were implemented to handle the creation and retrieval of wheel specification forms.

1. Create Wheel Specification
Creates a new wheel specification record in the database.

Endpoint: POST /api/forms/wheel-specifications

Description: Accepts a nested JSON object in the request body, validates it, and saves it to the database. It returns the newly created record, including its database-generated ID.

Success Response: 201 Created

Example Request Body:

{
  "formNumber": "WHEEL-TEST-001",
  "submittedBy": "test_user",
  "submittedDate": "2025-07-20",
  "fields": {
    "treadDiameterNew": "915 (900-1000)",
    "lastShopIssueSize": "837 (800-900)",
    "condemningDia": "825 (800-900)",
    "wheelGauge": "1600 (+2,-1)",
    "variationSameAxle": "0.5",
    "variationSameBogie": "5",
    "variationSameCoach": "13",
    "wheelProfile": "29.4 Flange Thickness",
    "intermediateWWP": "20 TO 28",
    "bearingSeatDiameter": "130.043 TO 130.068",
    "rollerBearingOuterDia": "280 (+0.0/-0.035)",
    "rollerBearingBoreDia": "130 (+0.0/-0.025)",
    "rollerBearingWidth": "93 (+0/-0.250)",
    "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
    "wheelDiscWidth": "127 (+4/-0)"
  }
}

2. Get Wheel Specifications
Retrieves a list of all wheel specification records.

Endpoint: GET /api/forms/wheel-specifications

Description: Fetches all wheel specification records currently stored in the database. It supports pagination via skip and limit query parameters.

Success Response: 200 OK

Example Success Response:

[
  {
    "id": 1,
    "formNumber": "WHEEL-TEST-001",
    "submittedBy": "test_user",
    "submittedDate": "2025-07-20",
    "fields": {
      "treadDiameterNew": "915 (900-1000)",
      "lastShopIssueSize": "837 (800-900)",
      "condemningDia": "825 (800-900)",
      "wheelGauge": "1600 (+2,-1)",
      "variationSameAxle": "0.5",
      "variationSameBogie": "5",
      "variationSameCoach": "13",
      "wheelProfile": "29.4 Flange Thickness",
      "intermediateWWP": "20 TO 28",
      "bearingSeatDiameter": "130.043 TO 130.068",
      "rollerBearingOuterDia": "280 (+0.0/-0.035)",
      "rollerBearingBoreDia": "130 (+0.0/-0.025)",
      "rollerBearingWidth": "93 (+0/-0.250)",
      "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
      "wheelDiscWidth": "127 (+4/-0)"
    }
  }
]

Setup and Installation Instructions
To set up and run this project locally, please follow these steps:

1. Prerequisites:

Python 3.8+

pip (Python package installer)

A running PostgreSQL instance (local or cloud-hosted)

2. Clone the Repository:

Download and unzip the kpa_backend source code folder.

3. Set Up Virtual Environment:

Navigate to the project's root directory (kpa_backend) in your terminal.

Create and activate a virtual environment:

# Create the environment
python -m venv venv

# Activate the environment (Windows)
venv\Scripts\activate

# Activate the environment (macOS/Linux)
source venv/bin/activate

4. Install Dependencies:

Install all required packages using the requirements.txt file.

pip install -r requirements.txt

5. Configure the Database:

Open the app/database.py file.

Update the SQLALCHEMY_DATABASE_URL variable with your PostgreSQL connection string. Ensure any special characters in your password are URL-encoded (e.g., @ becomes %40).

Running the Server
Once the setup is complete, run the Uvicorn server from the project's root directory:

python -m uvicorn app.main:app --reload

The API will be available at http://127.0.0.1:8000.

Interactive API documentation (provided by Swagger UI) will be available at http://127.0.0.1:8000/docs.

Limitations and Assumptions
Authentication: The implemented endpoints do not include user authentication (e.g., JWT tokens), as the focus was on the core functionality of the form data APIs. The provided frontend code seemed to handle authorization separately.

Database Migrations: The database table is created automatically by SQLAlchemy on the first run if it doesn't exist. For a production environment, a database migration tool like Alembic would be used to manage schema changes and prevent data loss.

Error Handling: Basic error handling for database connection issues and Pydantic validation errors is in place. More comprehensive logging and monitoring would be added for a production system.