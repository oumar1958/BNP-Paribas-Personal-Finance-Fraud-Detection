# scripts/predict.py

import pandas as pd
import joblib

# Charger le modèle entraîné
model = joblib.load("modeles/model_xgb.pkl")

# Charger les données de test
X_test = pd.read_csv("donnees/X_test_8skS2ey.csv", low_memory=False)

# Encodage des colonnes texte (object) en numérique
for col in X_test.columns:
    if X_test[col].dtype == "object":
        X_test[col] = X_test[col].astype("category").cat.codes

# Prédire les probabilités de fraude
probas = model.predict_proba(X_test)[:, 1]

# Créer un DataFrame de soumission
soumission = pd.DataFrame({
    "ID": range(1, len(probas) + 1),
    "fraud_flag": probas
})

# Sauvegarder le fichier au format CSV
soumission.to_csv("soumission.csv", index=False)

print("✅ Prédictions générées et enregistrées dans soumission.csv")
