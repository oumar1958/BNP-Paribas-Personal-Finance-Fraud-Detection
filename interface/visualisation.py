import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def afficher_graphiques():
    st.subheader("Visualisation des données")

    # Exemple basique
    st.write("Voici une démonstration des types de produits achetés.")

    try:
        df = pd.read_csv("donnees/X_train_G3tdtEn.csv")
        if "item1" in df.columns:
            item_counts = df["item1"].value_counts().head(10)
            fig, ax = plt.subplots()
            item_counts.plot(kind="bar", ax=ax)
            st.pyplot(fig)
        else:
            st.warning("La colonne 'item1' est manquante dans le fichier.")
    except FileNotFoundError:
        st.error("Le fichier X_train_G3tdtEn.csv est introuvable.")
