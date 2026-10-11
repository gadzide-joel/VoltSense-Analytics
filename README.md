# ⚡ VoltSense Analytics : Smart Grid & AI Monitoring

> Système intelligent de supervision de microgrid, combinant l'acquisition IoT, une API RESTful haute performance, une base de données relationnelle, un tableau de bord en temps réel et un module d'intelligence artificielle (Machine Learning).

---

## 📌 Présentation du Projet
**VoltSense Analytics** est un projet de niveau Licence 3 (L3) en Génie Électrique. Il simule et surveille des paramètres électriques critiques (tension, courant, puissance, fréquence) tout en croisant ces données avec des variables environnementales (température extérieure) pour anticiper les instabilités du réseau et détecter les anomalies.

---

## 🏗️ Architecture Technique

```text
VoltSense-Analytics/
├── backend/                  # API FastAPI & Modèles de données SQLAlchemy
│   ├── database.py           # Configuration de la connexion PostgreSQL
│   ├── models.py             # Définition des tables SQL
│   ├── schemas.py            # Schémas de validation Pydantic
│   └── main.py               # Endpoints REST (POST/GET télémesures)
├── ai_model/                 # Module de Machine Learning (Scikit-Learn)
│   └── predict_anomalies.py  # Détection d'anomalies (Isolation Forest) & Prédiction
├── venv/                     # Environnement virtuel Python
├── simulateur.py             # Script IoT de génération de flux de données en temps réel
├── dashboard.html            # Interface web de supervision
├── .gitignore                # Fichiers ignorés par Git
└── README.md                 # Documentation du projet
```



---

## 🚀 Technologies Utilisées
* **Backend & API :** Python 3.12, FastAPI, Uvicorn, SQLAlchemy, Pydantic
* **Base de Données :** PostgreSQL (avec connecteur `pg8000`)
* **Intelligence Artificielle :** Scikit-Learn (`IsolationForest`, `LinearRegression`), Pandas, NumPy
* **Interface & Visualisation :** HTML5, CSS3, Chart.js

---

## ⚙️ Guide d'Installation et d'Exécution

### 1. Cloner le dépôt et activer l'environnement
git clone https://github.com/gadzide-joel/VoltSense-Analytics.git
cd VoltSense-Analytics
.\venv\Scripts\Activate

### 2. Lancer les services (dans des terminaux séparés)
- **API FastAPI :** `python -m uvicorn backend.main.app --reload`
- **Simulateur IoT :** `python simulateur.py`
- **Modèle d'IA :** `python ai_model/predict_anomalies.py`

### 3. Accéder au Dashboard
Ouvre simplement le fichier **`dashboard.html`** dans ton navigateur web pour visualiser les graphiques de tension et de puissance en temps réel, ainsi que l'état du réseau et la météo.

---
*Auteur : GADZIDE Komi Joël — Étudiant en Génie Électrique*
