from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.dialects.postgresql import JSONB # Use JSONB for efficiency
from .database import Base

# This class defines the 'wheel_specifications' table in your database.
class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"

    id = Column(Integer, primary_key=True, index=True)
    formNumber = Column(String, unique=True, index=True)
    submittedBy = Column(String, index=True)
    submittedDate = Column(Date)
    
    # The nested 'fields' object will be stored in this JSON column
    fields = Column(JSONB)
