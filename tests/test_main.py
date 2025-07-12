import os
import pandas as pd

def test_submission_file_exists():
    """Vérifie que le fichier soumission.csv est bien généré."""
    assert os.path.exists("soumission.csv"), "Le fichier soumission.csv n'a pas été généré"

def test_submission_file_format():
    """Vérifie que le fichier de soumission a les bonnes colonnes et le bon format."""
    df = pd.read_csv("soumission.csv")

    assert "ID" in df.columns, "La colonne 'ID' est manquante"
    assert "fraud_flag" in df.columns, "La colonne 'fraud_flag' est manquante"

    # Vérifie que la colonne fraud_flag est bien entre 0 et 1
    assert df["fraud_flag"].between(0, 1).all(), "Les valeurs de fraud_flag doivent être entre 0 et 1"

    # Vérifie que le nombre de lignes est cohérent
    assert len(df) > 0, "Le fichier de soumission est vide"
