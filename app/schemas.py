from pydantic import BaseModel, ConfigDict
from typing import Optional
import datetime

# Defines the nested 'fields' object inside the main request
class WheelSpecificationFields(BaseModel):
    treadDiameterNew: str
    lastShopIssueSize: str
    condemningDia: str
    wheelGauge: str
    variationSameAxle: str
    variationSameBogie: str
    variationSameCoach: str
    wheelProfile: str
    intermediateWWP: str
    bearingSeatDiameter: str
    rollerBearingOuterDia: str
    rollerBearingBoreDia: str
    rollerBearingWidth: str
    axleBoxHousingBoreDia: str
    wheelDiscWidth: str

# Defines the main request body for creating a new specification
class WheelSpecificationCreate(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: datetime.date
    fields: WheelSpecificationFields

# Defines the full schema for the data returned by the API, including the database ID
class WheelSpecification(BaseModel):
    id: int
    formNumber: str
    submittedBy: str
    submittedDate: datetime.date
    fields: WheelSpecificationFields

    # Replaces the old 'orm_mode = True' for Pydantic V2
    model_config = ConfigDict(from_attributes=True)
