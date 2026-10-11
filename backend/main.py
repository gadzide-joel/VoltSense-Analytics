from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas
from .database import engine, get_db

# Création automatique des tables dans PostgreSQL
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="VoltSense Analytics API",
    description="API IoT de surveillance de la qualité électrique et santé machine",
    version="1.0.0"
)

# Configuration CORS pour autoriser le dashboard web
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API VoltSense Analytics"}

@app.post("/api/v1/telemetry", response_model=schemas.TelemetryResponse)
def create_telemetry(telemetry: schemas.TelemetryCreate, db: Session = Depends(get_db)):
    db_telemetry = models.Telemetry(
        device_id=telemetry.device_id,
        voltage=telemetry.voltage,
        current=telemetry.current,
        power=telemetry.power,
        frequency=telemetry.frequency,
        temperature=telemetry.temperature
    )
    db.add(db_telemetry)
    db.commit()
    db.refresh(db_telemetry)
    return db_telemetry

@app.get("/api/v1/telemetry", response_model=List[schemas.TelemetryResponse])
def get_telemetries(limit: int = 20, db: Session = Depends(get_db)):
    records = db.query(models.Telemetry).order_by(models.Telemetry.id.desc()).limit(limit).all()
    return records
