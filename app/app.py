import streamlit as st
import pandas as pd
import base64

# --- FOND D'ÉCRAN ---
def set_background(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: top center;
            background-attachment: fixed;
        }}
        .block-container {{
            max-width: 100%;
            padding: 2rem 5rem;
            background-color: transparent;
        }}
        </style>
    """, unsafe_allow_html=True)

# --- POLICE POKÉMON ---
def load_custom_font(font_path):
    with open(font_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(f"""
        <style>
        @font-face {{
            font-family: 'Pokemon';
            src: url("data:font/ttf;base64,{encoded}") format("truetype");
            font-display: swap;
        }}
        .intro-box {{
            background: rgba(255, 255, 255, 0.92);
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
            text-align: center;
            margin: 30px auto;
            max-width: 800px;
            margin-top: -40px !important;
            position: relative;
            z-index: 10;
        }}
        .pokemon-title {{
            font-family: 'Pokemon', sans-serif !important;
            font-size: 20px !important;
            color: #FFCB05 !important;
            text-shadow: 3px 3px 0 #2C72B8, -1px -1px 0 #2C72B8,
                         1px -1px 0 #2C72B8, -1px 1px 0 #2C72B8,
                         1px 1px 0 #2C72B8 !important;
            margin-bottom: 20px !important;
            letter-spacing: 2px !important;
            animation: glow 2s ease-in-out infinite alternate !important;
            text-transform: uppercase !important;
        }}
        .intro-text {{
            font-size: 15px;
            color: #2c3e50;
            line-height: 1.6;
            font-family: 'Pokemon', Arial, sans-serif;
            text-align: center;
            margin: 0 auto;
            max-width: 700px;
            letter-spacing: 1px;
        }}
        @keyframes glow {{
            from {{ text-shadow: 0 0 5px #FFCB05 !important; }}
            to {{ text-shadow: 0 0 10px #FFCB05, 0 0 20px #2C72B8 !important; }}
        }}
        </style>
    """, unsafe_allow_html=True)

# --- Initialisation ---
set_background("assets/background.png")
load_custom_font("assets/fonts/Pokemon.ttf")

# --- HEADER ---
col1, col2 = st.columns([2, 1])
with col1:
    st.image("assets/Palworld_Logo.png", width=400)
with col2:
    st.image("assets/Animation - 1748786391845.gif", width=550)

# --- INTRODUCTION + BOUTON ---
st.markdown("""
    <div class="intro-box">
        <h2 class="pokemon-title"> BIENVENUE DANS LE PALWORLD COMBAT DASHBOARD</h2>
        <p class="intro-text">
            🔍 EXPLORE LES DONNÉES DE TES PALS PRÉFÉRÉS<br><br>
            ⚔️ CONSTRUIS L'ÉQUIPE PARFAITE POUR DOMINER PALWORLD<br><br>
            💥 DÉCOUVRE LES PLUS PUISSANTS ET LES PLUS RARES
        </p>
        <div style="margin-top: 30px;">
            <a href="#dashboard" style="
                background-color: #FFCB05;
                color: white;
                padding: 12px 25px;
                border-radius: 10px;
                font-size: 18px;
                text-decoration: none;
                font-weight: bold;
                box-shadow: 0 4px 10px rgba(0,0,0,0.3);
                transition: background 0.3s;
            " onmouseover="this.style.backgroundColor='#1f5a99'" onmouseout="this.style.backgroundColor='#2C72B8'">
                🚀 Commencer
            </a>
        </div>
    </div>
    <div id="dashboard"></div>
""", unsafe_allow_html=True)

# --- CHARGEMENT DES DONNÉES ---
@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned/combat_attribute_cleaned.csv")

df = load_data()

# --- FILTRES ---
with st.sidebar:
    st.header("🎯 Filtres")
    names = st.multiselect("🔎 Nom du Pal", options=df["name"].unique(), default=[])
    tribes = st.multiselect("🧬 Tribu", options=df["tribe"].unique(), default=[])
    classes = st.multiselect("🏷️ Classe", options=df["bp_class"].unique(), default=[])

if names:
    df = df[df["name"].isin(names)]
if tribes:
    df = df[df["tribe"].isin(tribes)]
if classes:
    df = df[df["bp_class"].isin(classes)]

# --- TABLEAU ---
st.subheader("📋 Tableau des Pals")
st.dataframe(df[["name", "bp_class", "tribe", "lv5", "price", "skill_description"]])

# --- ONGLET D'ANALYSE ---
tab1, tab2, tab3 = st.tabs(["📊 Niveaux max (lv5)", "💰 Prix", "🔍 Détails"])

with tab1:
    st.subheader("📊 Distribution des niveaux max (lv5)")
    chart_data = df.set_index("name")["lv5"].sort_values(ascending=False)
    st.bar_chart(chart_data)

with tab2:
    st.subheader("💰 Répartition des prix")
    price_data = df.set_index("name")["price"].sort_values(ascending=False)
    st.bar_chart(price_data)

with tab3:
    st.subheader("🧠 Détails sur un Pal")
    selected = st.selectbox("Choisis un Pal :", df["name"].unique())
    with st.expander("🔎 Résultats détaillés", expanded=True):
        st.write(df[df["name"] == selected].T)

# --- FOOTER (affiché seulement à la fin de page) ---
st.markdown("""
<div style="text-align:center; padding:10px; color:#fff; background:#2c3e50; border-radius:10px; margin-top:30px;">
    © 2024 Palworld Combat Dashboard | Créé avec ❤️ par <strong>Dina / Rayanne / Nassima</strong>
</div>
""", unsafe_allow_html=True)
