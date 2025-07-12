# scripts/preprocessing.py

import pandas as pd

def load_data(x_path, y_path):
    X = pd.read_csv(x_path, low_memory=False)
    y = pd.read_csv(y_path, low_memory=False)

    # 🟢 S'assurer que y est une Series (extrait seulement la colonne cible)
    if "fraud_flag" in y.columns:
        y = y["fraud_flag"]
    elif y.shape[1] == 1:
        y = y.iloc[:, 0]

    return X, y

