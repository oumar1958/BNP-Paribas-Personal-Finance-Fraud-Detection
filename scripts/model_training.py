import pandas as pd
import xgboost as xgb
from sklearn.metrics import average_precision_score
from sklearn.model_selection import train_test_split
import joblib

def train_model():
    # Chargement des données prétraitées
    X = pd.read_csv("donnees/X_train_G3tdtEn.csv", low_memory=False)
    y = pd.read_csv("donnees/Y_train_2_XPXJDyy.csv")["fraud_flag"]

  # Encodage automatique des colonnes catégorielles
    for col in X.columns:
        if X[col].dtype == "object":
            X[col] = X[col].astype("category").cat.codes
    # Séparation train/validation
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    # Initialisation du modèle XGBoost
    model = xgb.XGBClassifier(
        objective='binary:logistic',
        eval_metric='aucpr',
        use_label_encoder=False,
        scale_pos_weight=(len(y) - sum(y)) / sum(y),  # Gestion du déséquilibre
        random_state=42
    )

    # Entraînement
    model.fit(X_train, y_train)

    # Prédiction sur validation
    y_val_pred = model.predict_proba(X_val)[:, 1]

    # Évaluation avec PR-AUC
    pr_auc = average_precision_score(y_val, y_val_pred)
    print(f"PR-AUC sur le jeu de validation : {pr_auc:.4f}")

    # Sauvegarde du modèle entraîné
    joblib.dump(model, "modeles/model_xgb.pkl")
    print("✅ Modèle sauvegardé sous modeles/model_xgb.pkl")

if __name__ == "__main__":
    train_model()
