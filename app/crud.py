from sqlalchemy.orm import Session
from . import models, schemas
from typing import List


def get_wheel_specifications(db: Session, skip: int = 0, limit: int = 100) -> List[models.WheelSpecification]:
    return db.query(models.WheelSpecification).offset(skip).limit(limit).all()



def create_wheel_specification(db: Session, spec: schemas.WheelSpecificationCreate) -> models.WheelSpecification:
 
    db_spec = models.WheelSpecification(**spec.dict())
    
  
    db.add(db_spec)
    
    db.commit()
  
    db.refresh(db_spec)
    
    return db_spec

