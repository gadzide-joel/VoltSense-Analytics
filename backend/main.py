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

# --- AJOUT DU CORS POUR LE DASHBOARD ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autorise n'importe quelle page web à se connecter
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ---------------------------------------

@app.get("/")

def root():
    return {
        "system": "VoltSense Analytics",
        "status": "online",
        "message": "Bienvenue sur l'API de surveillance industrielle"
    }

# Endpoint pour recevoir les données envoyées par les boîtiers ESP32
@app.post("/api/v1/telemetry", response_model=schemas.TelemetryResponse)
def receive_telemetry(data: schemas.TelemetryCreate, db: Session = Depends(get_db)):
    db_telemetry = models.Telemetry(
        device_id=data.device_id,
        voltage=data.voltage,
        current=data.current,
        power=data.power,
        frequency=data.frequency
    )
    db.add(db_telemetry)
    
    # Détection automatique d'anomalie de tension (ex: réseau togolais / CEET)
    if data.voltage > 245.0:
        alert = models.Alert(
            device_id=data.device_id,
            alert_type="Surtension",
            severity="CRITICAL",
            message=f"Tension anormale détectée : {data.voltage}V"
        )
        db.add(alert)
    elif data.voltage < 195.0:
        alert = models.Alert(
            device_id=data.device_id,
            alert_type="Baisse de tension",
            severity="WARNING",
            message=f"Chute de tension détectée : {data.voltage}V"
        )
        db.add(alert)

    db.commit()
    db.refresh(db_telemetry)
    return db_telemetry

# Endpoint pour récupérer l'historique des relevés
@app.get("/api/v1/telemetry", response_model=List[schemas.TelemetryResponse])
def get_telemetry_history(limit: int = 50, db: Session = Depends(get_db)):
    return db.query(models.Telemetry).order_by(models.Telemetry.timestamp.desc()).limit(limit).all()