# tests/test_predict.py

import pandas as pd
import os

def test_submission_file():
    assert os.path.exists("soumission.csv"), "Le fichier soumission.csv n'existe pas"
    df = pd.read_csv("soumission.csv")
    assert "ID" in df.columns
    assert "fraud_flag" in df.columns
    assert df["fraud_flag"].between(0, 1).all(), "Les valeurs doivent être entre 0 et 1"
