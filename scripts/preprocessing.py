# scripts/preprocessing.py

import pandas as pd
import numpy as np

def load_data(x_path, y_path=None):
    X = pd.read_csv(x_path)
    if y_path:
        y = pd.read_csv(y_path)
        return X, y
    return X

def preprocess_data(X):
    # Créer une colonne : valeur totale du panier
    cash_price_cols = [col for col in X.columns if "cash_price" in col]
    X["total_cash_price"] = X[cash_price_cols].sum(axis=1)

    # Créer une colonne : nombre total de produits achetés
    prod_count_cols = [col for col in X.columns if "Nbr_of_prod_purchas" in col]
    X["total_quantity"] = X[prod_count_cols].sum(axis=1)

    # Créer une colonne : prix moyen par produit (en évitant les divisions par zéro)
    X["avg_price_per_product"] = X["total_cash_price"] / (X["total_quantity"] + 1e-5)

    # Supprimer les colonnes textuelles inutiles pour ce projet de base
    cols_to_drop = [col for col in X.columns if any(k in col for k in ["item", "make", "model", "goods_code"])]
    X.drop(columns=cols_to_drop, inplace=True)

    return X

def save_preprocessed(X, path):
    X.to_csv(path, index=False)
