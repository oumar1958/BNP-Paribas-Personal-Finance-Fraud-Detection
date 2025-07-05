## 🔍 Objectif

Ce projet vise à identifier les transactions suspectes en exploitant les données paniers et en analysant les comportements frauduleux.

## 📊 Fonctionnalités

- Détection de fraudes dans les transactions financières
- Analyse des comportements suspects
- Traitement et préparation des données paniers
- Modélisation et prédiction des fraudes
- Interface de visualisation interactive

## 🧩 Configuration et utilisation

### Exigences

- Python 3.x 🐍
- Environnement virtuel Python (recommandé)

### Installation

1. Cloner le projet :
```bash
git clone <repository-url>
cd <nom_du_projet>
```

2. Configurer l'environnement virtuel :
```bash
python -m venv .venv

# Activation (selon votre système)
# Linux/macOS:
source .venv/bin/activate

# Windows CMD:
.venv\Scripts\activate.bat

# Windows PowerShell:
.venv\Scripts\Activate.ps1
```

3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

### Lancement
```bash
python ./scripts/main.py
```

## 📂 Structure du projet

```
├── donnees/                   # Jeux de données
│   ├── x_train.csv           # Variables explicatives (entraînement)
│   ├── y_train.csv           # Variable cible (entraînement)
│   ├── x_test.csv            # Variables explicatives (test)
│   └── submission_example.csv # Exemple de soumission
│
├── document/                  # Documentation
│   ├── Report.docx          # Documentation détaillée
│   ├── Report_fraud_detector.pdf # Rapport final
│   ├── Roadmap.png          # Planning du projet
│   ├── presentations/       # Présentations
│   └── logigramme.png       # Schéma système
│
├── scripts/                  # Scripts Python
│   ├── main.py              # Script principal
│   ├── preprocessing.py     # Traitement des données
│   ├── model_training.py    # Entraînement du modèle
│   ├── predict.py           # Génération des prédictions
│   └── feature_engineering.py # Générations de features
│
├── interface/               # Interface utilisateur
│   ├── dashboard.py        # Interface interactive
│   ├── menu.py            # Navigation
│   └── visualisation.py    # Graphiques
│
└── tests/                  # Tests unitaires
    ├── test_main.py       # Tests principaux
    ├── test_preprocessing.py # Tests de preprocessing
    ├── test_model_training.py # Tests d'entraînement
    └── test_predict.py     # Tests de prédiction
```

## 📚 Jeu de données

- **Source** : Données fournies par BNP Paribas Personal Finance
- **Taille** : 115 988 observations
- **Colonnes** : 147 variables
- **Variable cible** : `fraud_flag` (1 = fraude, 0 = non fraude)
- **Taux de fraude** : 1,4%

## 📊 Métrique d'évaluation

- PR-AUC (Precision-Recall Area Under Curve)
- Utilisation de `average_precision_score` de scikit-learn

## 🎯 Benchmarks

| Modèle | PR-AUC |
|--------|--------|
| Modèle aléatoire | 0,017 |
| Modèle ML avec preprocessing | 0,14 |

## 📄 Format de soumission

Le fichier de soumission doit être un fichier .csv avec les colonnes :
- `ID`
- `fraud_flag`

Exemple :
```
ID,fraud_flag
1,0.78
2,0.03
```


## 🤝 Contribuer

1. Fork le projet
2. Créez une branche (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push à la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## Auteurs

Oumar Abdramane ALLAWAN
