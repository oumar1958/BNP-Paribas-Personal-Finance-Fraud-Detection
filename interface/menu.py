import streamlit as st

def afficher_menu():
    menu = ["Accueil", "Exploration des données", "Prédictions"]
    choix = st.sidebar.selectbox("Navigation", menu)
    return choix
