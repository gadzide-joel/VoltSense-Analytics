import pandas as pd
from sqlalchemy import create_engine
from sklearn.ensemble import IsolationForest
from sklearn.linear_model import LinearRegression
import numpy as np

DB_URL = "postgresql+pg8000://postgres:joegad0101@localhost:5432/voltsense_db"
engine = create_engine(DB_URL)

def run_advanced_analytics():
    query = "SELECT timestamp, voltage, current, power, temperature FROM telemetries ORDER BY timestamp ASC;"
    df = pd.read_sql(query, con=engine)

    if df.empty:
        print("Aucune donnée disponible dans la base de données.")
        return

    print(f"--- Données chargées : {len(df)} enregistrements ---")

    # 1. Détection d'anomalies (Isolation Forest)
    iso = IsolationForest(contamination=0.05, random_state=42)
    df['anomaly'] = iso.fit_predict(df[['voltage', 'current', 'power']])
    
    nb_anomalies = (df['anomaly'] == -1).sum()
    print(f"[IA ANOMALIES] {nb_anomalies} anomalies détectées sur l'historique.")

    # 2. Prévision de charge influencée par la Météo
    df['time_index'] = np.arange(len(df))
    X = df[['time_index', 'temperature']]
    y = df['power']

    model = LinearRegression()
    model.fit(X, y)

    future_X = pd.DataFrame({
        'time_index': [len(df) + i for i in range(1, 4)],
        'temperature': [32.5, 33.0, 33.5]
    })
    
    future_pred = model.predict(future_X)
    print("\n[PREVISION METEO & CHARGE] Puissance estimée selon la température extérieure :")
    for i, p in enumerate(future_pred, start=1):
        print(f"  + Heure +{i} : {p:.2f} Watts prévus")

if __name__ == "__main__":
    run_advanced_analytics()