import os
import streamlit as st
import nltk

# 🔐 Forcer NLTK à utiliser le dossier local
nltk_data_path = os.path.join(os.path.dirname(__file__), "nltk_data")
nltk.data.path.append(nltk_data_path)

# 🚫 Bloquer les téléchargements automatiques
def disable_nltk_download(*args, **kwargs):
    raise RuntimeError("NLTK download disabled in cloud environment")

nltk.download = disable_nltk_download

# 📦 Modules ICARE
from user_onboarding import run_onboarding
from training_UI import run_training_ui
from quiz_UI import run_quiz_ui
from document_uploader import run_uploader
from global_settings import load_settings

# ⚙️ Chargement des paramètres globaux
settings = load_settings()

# 🧭 Barre latérale pour navigation
st.sidebar.title("🧭 Navigation ICARE")
choice = st.sidebar.radio("Choisissez une section :", [
    "👋 Accueil & Onboarding",
    "📚 Formation interactive",
    "🧪 Quiz & Évaluation",
    "📄 Ingestion de documents"
])

# 🧩 Affichage dynamique selon le choix
if choice == "👋 Accueil & Onboarding":
    run_onboarding(settings)

elif choice == "📚 Formation interactive":
    run_training_ui(settings)

elif choice == "🧪 Quiz & Évaluation":
    run_quiz_ui(settings)

elif choice == "📄 Ingestion de documents":
    run_uploader(settings)

# 🧼 Footer pédagogique
st.markdown("---")
st.caption("🔧 ICARE Launcher – conçu pour la robustesse terrain et la transmission locale.")
