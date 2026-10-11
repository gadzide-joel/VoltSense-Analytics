from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from .database import Base

class Telemetry(Base):
    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, index=True)
    voltage = Column(Float, nullable=False)   # Tension (V)
    current = Column(Float, nullable=False)   # Courant (A)
    power = Column(Float, nullable=False)     # Puissance (W)
    frequency = Column(Float, default=50.0)   # Fréquence (Hz)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, index=True)
    alert_type = Column(String, nullable=False) # Ex: Surtension, Baisse de tension
    severity = Column(String, default="WARNING") # WARNING, CRITICAL
    message = Column(String)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())