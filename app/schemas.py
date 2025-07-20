from pydantic import BaseModel, ConfigDict
from typing import Optional
import datetime


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

class WheelSpecificationCreate(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: datetime.date
    fields: WheelSpecificationFields

class WheelSpecification(BaseModel):
    id: int
    formNumber: str
    submittedBy: str
    submittedDate: datetime.date
    fields: WheelSpecificationFields

  
    model_config = ConfigDict(from_attributes=True)
