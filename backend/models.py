from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from .database import Base

class Telemetry(Base):
    __tablename__ = "telemetries"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, index=True)
    voltage = Column(Float)
    current = Column(Float)
    power = Column(Float)
    frequency = Column(Float)
    temperature = Column(Float, default=30.0)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
