# tests/test_model_training.py

import os
import joblib

def test_model_existence():
    assert os.path.exists("modeles/model_xgb.pkl"), "Le modèle n'a pas été sauvegardé"
    model = joblib.load("modeles/model_xgb.pkl")
    assert hasattr(model, "predict_proba"), "Le modèle ne possède pas la méthode predict_proba"
