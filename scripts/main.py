# scripts/main.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts import preprocessing

# Charger les données
X_train, y_train = preprocessing.load_data("donnees/X_train_G3tdtEn.csv", "donnees/Y_train_2_XPXJDyy.csv")




# Prétraiter les données
X_train_processed = preprocessing.preprocess_data(X_train)

# Sauvegarder
preprocessing.save_preprocessed(X_train_processed, "donnees/x_train_clean.csv")
y_train.to_csv("donnees/y_train_clean.csv", index=False)
