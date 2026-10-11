from pydantic import BaseModel
from datetime import datetime

class TelemetryBase(BaseModel):
    device_id: str
    voltage: float
    current: float
    power: float
    frequency: float
    temperature: float = 30.0

class TelemetryCreate(TelemetryBase):
    pass

class TelemetryResponse(TelemetryBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True