from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TelemetryCreate(BaseModel):
    device_id: str
    voltage: float
    current: float
    power: float
    frequency: Optional[float] = 50.0

class TelemetryResponse(TelemetryCreate):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True

class AlertResponse(BaseModel):
    id: int
    device_id: str
    alert_type: str
    severity: str
    message: str
    timestamp: datetime

    class Config:
        from_attributes = True