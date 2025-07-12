import streamlit as st
import pandas as pd
import joblib
import os
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

# === CONFIGURATION ===
st.set_page_config(
    page_title="Détection de Fraude",
    layout="wide",
    initial_sidebar_state="expanded"
)

# === CHARGEMENT DU MODÈLE ===
@st.cache_resource
def load_model():
    return joblib.load("modeles/model_xgb.pkl")

model = load_model()

# === PIPELINE DE PRÉTRAITEMENT UNIVERSEL ===
def detect_and_build_pipeline(df):
    cat_cols = df.select_dtypes(include=["object", "category", "bool"]).columns.tolist()
    num_cols = df.select_dtypes(include=["int", "float"]).columns.tolist()

    num_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="mean")),
        ("scaler", StandardScaler())
    ])

    cat_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore", sparse=False))
    ])

    preprocessor = ColumnTransformer(transformers=[
        ("num", num_pipeline, num_cols),
        ("cat", cat_pipeline, cat_cols)
    ])

    return preprocessor, cat_cols, num_cols

# === Titre principal ===
st.title("🏦 Détection de Fraude - BNP Paribas Personal Finance")
st.markdown("Ce tableau de bord permet de prédire si un panier client présente une **probabilité de fraude**.")

# === MENU DE NAVIGATION ===
menu = st.sidebar.radio("Navigation", ["📂 Chargement des données", "🔍 Prédiction de fraude", "📊 A propos"])

# === PAGE : Chargement de données ===
if menu == "📂 Chargement des données":
    st.header("📁 Charger un panier client")

    uploaded_file = st.file_uploader("Téléversez un fichier CSV contenant un panier client :", type=["csv"])

    if uploaded_file is not None:
        try:
            input_data = pd.read_csv(uploaded_file)
            st.success("✅ Fichier chargé avec succès !")
            st.write("Aperçu des données :", input_data.head())
            st.session_state["input_data"] = input_data
        except Exception as e:
            st.error(f"❌ Erreur de lecture du fichier : {e}")

# === PAGE : Prédiction ===
elif menu == "🔍 Prédiction de fraude":
    st.header("🔎 Prédire la probabilité de fraude")

    if "input_data" in st.session_state:
        X_input = st.session_state["input_data"]

        try:
            # Construction pipeline et transformation
            preprocessor, cat_cols, num_cols = detect_and_build_pipeline(X_input)
            X_transformed = preprocessor.fit_transform(X_input)

            # Prédiction
            proba_fraude = model.predict_proba(X_transformed)[:, 1]
            df_result = X_input.copy()
            df_result["Probabilité de fraude"] = proba_fraude

            st.subheader("Résultats de la prédiction :")
            st.dataframe(df_result[["Probabilité de fraude"]], use_container_width=True)

            seuil = st.slider("Seuil de détection (entre 0 et 1)", 0.0, 1.0, 0.5)
            decisions = (proba_fraude > seuil).astype(int)
            df_result["Décision"] = decisions

            st.write("🔒 **0 = panier normal | 1 = suspicion de fraude**")
            st.dataframe(df_result[["Probabilité de fraude", "Décision"]], use_container_width=True)

        except Exception as e:
            st.error(f"❌ Erreur pendant la prédiction : {e}")
    else:
        st.warning("⚠️ Veuillez d'abord charger un panier client via l'onglet 'Chargement des données'.")

# === PAGE : À propos ===
elif menu == "📊 A propos":
    st.header("ℹ️ Informations sur le projet")
    st.markdown("""
    - **Projet :** Détection de fraude sur les paniers clients financés par BNP Paribas Personal Finance  
    - **Objectif :** Prédire si un panier est potentiellement frauduleux  
    - **Modèle :** XGBoost entraîné avec une PR-AUC de 0.25  
    - **Auteur :** Oumar  
    """)

    if os.path.exists("document/logigramme.png"):
        st.image("document/logigramme.png", caption="Logigramme du projet", use_container_width=True)
    else:
        st.warning("📄 Image logigramme introuvable.")
