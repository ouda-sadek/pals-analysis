import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64

# 🌈 Configuration de la page
st.set_page_config(page_title="Palworld Boss Explorer", layout="wide")

# 🖼️ Appliquer un fond d'écran depuis une image locale
def set_bg_from_local(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 🔧 Charger le fond
set_bg_from_local("assets/background.jpg")

# 🧠 Chargement et nettoyage des données
df = pd.read_csv("data/Palworld_Data-comparison of ordinary BOSS attributes.csv")
df.columns = ['name', 'HP', 'name_1', 'species', 'Remote attack', 'name_2', 'Riding speed', 'extra']
df.drop(columns='extra', inplace=True)

df["HP"] = pd.to_numeric(df["HP"], errors="coerce")
df["Remote attack"] = pd.to_numeric(df["Remote attack"], errors="coerce")
df["Riding speed"] = pd.to_numeric(df["Riding speed"], errors="coerce")
df.dropna(subset=["HP"], inplace=True)

# 💅 Style personnalisé
st.markdown("""
    <style>
    h1 {
        text-align: center;
        font-size: 3em;
        color: #3f51b5;
        text-shadow: 2px 2px 5px #000;
    }
    .block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# 🎮 Logo et titre
st.image("assets/palworld_logo.png", width=500)
st.markdown("<h1>🎮 Palworld Boss Explorer</h1>", unsafe_allow_html=True)
st.markdown("Analyse visuelle et fun des attributs des Boss dans Palworld.")

# 🧩 Filtres interactifs
species_filter = st.selectbox("🔍 Filtrer par espèce (species)", options=["Tous"] + sorted(df["species"].dropna().unique().tolist()))
if species_filter != "Tous":
    df = df[df["species"] == species_filter]

# 🧮 Attributs & options
sort_option = st.selectbox("📊 Choisir l’attribut pour trier :", ["HP", "Remote attack", "Riding speed"])
top_n = st.slider("🔢 Nombre de Boss à afficher :", min_value=5, max_value=20, value=10)
palette_choice = st.selectbox("🎨 Choisir une palette de couleurs :", ["coolwarm", "magma", "rocket", "viridis", "plasma"])

# 📊 Graphique
st.subheader(f"🔥 Top {top_n} Boss par {sort_option}")
top_df = df.sort_values(sort_option, ascending=False).head(top_n)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=top_df, x=sort_option, y="name", palette=palette_choice, ax=ax)
ax.set_title(f"Top {top_n} Boss selon {sort_option}", fontsize=14)
ax.set_xlabel(sort_option)
ax.set_ylabel("Nom du Boss")
st.pyplot(fig)

# 🧾 Footer
st.markdown("---")
st.markdown("👩‍💻 Réalisé par Dina – Étudiante IA & Data @ La Plateforme_", unsafe_allow_html=True)
