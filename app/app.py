import streamlit as st
import pandas as pd

# --- Chargement des données ---
@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned/combat_attribute_cleaned.csv")

df = load_data()

st.title("🔍 Exploration des Pals – Palworld Combat Attributes")

# --- Filtres ---
st.sidebar.header("Filtres")

# Filtre par nom
names = st.sidebar.multiselect("Nom du Pal", options=df["name"].unique(), default=[])
if names:
    df = df[df["name"].isin(names)]

# Filtre par tribu
tribes = st.sidebar.multiselect("Tribu", options=df["tribe"].unique(), default=[])
if tribes:
    df = df[df["tribe"].isin(tribes)]

# Filtre par classe
classes = st.sidebar.multiselect("Classe", options=df["bp_class"].unique(), default=[])
if classes:
    df = df[df["bp_class"].isin(classes)]

# --- Aperçu de la table filtrée ---
st.subheader("📋 Table des Pals")
st.dataframe(df[["name", "bp_class", "tribe", "lv5", "price", "skill_description"]])

# --- Histogrammes ---
st.subheader("📊 Distribution des niveaux max (lv5)")
st.bar_chart(df.set_index("name")["lv5"].sort_values(ascending=False))

st.subheader("💰 Répartition des prix")
st.bar_chart(df.set_index("name")["price"].sort_values(ascending=False))

# --- Détail optionnel ---
st.subheader("🧠 Détails d'un Pal")
selected = st.selectbox("Sélectionne un Pal", df["name"].unique())
st.write(df[df["name"] == selected].T)
