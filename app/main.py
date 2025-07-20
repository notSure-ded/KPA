from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

# Import the CORS middleware
from fastapi.middleware.cors import CORSMiddleware

# These imports now point to your corrected files
from . import crud, models, schemas
from .database import SessionLocal, engine

# This creates the database table based on your corrected models.py
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="KPA Forms API")


# --- Add CORS Middleware ---
# This allows your browser to communicate with the API.
origins = [
    "*",  # Allows all origins for development purposes
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


# --- Dependency ---
# This function provides a database session to the API endpoints.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# --- API Endpoints ---

@app.post("/api/forms/wheel-specifications", response_model=schemas.WheelSpecification, status_code=201)
def create_wheel_spec_endpoint(
    spec: schemas.WheelSpecificationCreate, db: Session = Depends(get_db)
):
    """
    Create a new wheel specification record.
    The request body should be a JSON object matching the corrected WheelSpecificationCreate schema.
    """
    # Optional: Check if a form with this number already exists
    db_form = db.query(models.WheelSpecification).filter(models.WheelSpecification.formNumber == spec.formNumber).first()
    if db_form:
        raise HTTPException(status_code=400, detail=f"Form with number {spec.formNumber} already exists.")
    
    return crud.create_wheel_specification(db=db, spec=spec)


@app.get("/api/forms/wheel-specifications", response_model=List[schemas.WheelSpecification])
def read_wheel_specs_endpoint(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    """
    Retrieve a list of all wheel specification records.
    You can use the 'skip' and 'limit' query parameters for pagination.
    """
    specs = crud.get_wheel_specifications(db, skip=skip, limit=limit)
    return specs
