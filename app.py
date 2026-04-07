import streamlit as st
import base64
from datetime import datetime
import uuid
import firebase_admin
from firebase_admin import credentials, firestore, storage
import os

# ---------------------- FIREBASE CONFIG ----------------------
SERVICE_ACCOUNT_PATH = r"C:\Users\Geetha Kola\Downloads\serviceAccountKey.json"
STORAGE_BUCKET = "Kisan Saathi-8bcf9.appspot.com"

if not firebase_admin._apps:
    cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
    firebase_admin.initialize_app(cred, {
        "storageBucket": STORAGE_BUCKET
    })

db = firestore.client()
bucket = storage.bucket(STORAGE_BUCKET)

# ---------------------- USER SESSION ----------------------
if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(page_title="Kisan Saathi", layout="wide")

# ---------------------- BG IMAGE LOADER ----------------------
def get_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

img_path = "Farmer in the Golden Sunset.png"
img_base64 = get_base64(img_path)

# ---------------------- TRANSLATIONS ----------------------
translations = {
    "en": {
        "title": "🌱 Kisan Saathi",
        "Farm Tools": "Farm Tools",
        "Marketplace": "Marketplace",
        "Crop": "Crop",
        "Fertilizer & Orders": "Fertilizer & Orders",
        "Chatbot": "Chatbot",
        "Weather": "Weather",
        "Community": "Community ",
        "Expert Consultation": "Expert Consultation",
        "Government Schemes": "Government Schemes",
        "News": "News",
        
    },
    "hi": {
        "title": "🌱 किसान साथी",
        "Farm Tools": "खेती के औज़ार",
        "Marketplace": "बाज़ार",
        "Crop": "फ़सल",
        "Fertilizer & Orders": "उर्वरक व आदेश",
        "Chatbot": "चैटबॉट",
        "Weather": "मौसम",
        "Community Forum": "समुदाय मंच",
        "Expert Consultation": "विशेषज्ञ परामर्श",
        "Government Schemes": "सरकारी योजनाएँ",
        "News & Market Insights": "समाचार और बाजार अंतर्दृष्टि",
        
    },
    "te": {
        "title": "🌱 కిసాన్ సాథీ",
        "Farm Tools": "వ్యవసాయ పరికరాలు",
        "Marketplace": "మార్కెట్",
        "Crop": "పంట",
        "Fertilizer & Orders": "ఎరువులు & ఆర్డర్లు",
        "Chatbot": "చాట్‌బాట్",
        "Weather": "వాతావరణం",
        "Community Forum": "సముదాయం ఫోరమ్",
        "Expert Consultation": "నిపుణుల సలహా",
        "Government Schemes": "ప్రభుత్వ పథకాలు",
        "News & Market Insights": "సమాచారాలు & మార్కెట్ అవగాహనలు",
        
    }
}

# ---------------------- LANGUAGE SELECTION ----------------------
lang_choice = st.sidebar.selectbox("🌐 Select Language", ["English", "हिन्दी", "తెలుగు"])
lang_code = {"English": "en", "हिन्दी": "hi", "తెలుగు": "te"}[lang_choice]
st.session_state.lang = lang_code  # SAVE globally

# ---------------------- TOOL OPTIONS ----------------------
tool_options = [
    {"label": "Farm Tools", "icon": "🚜", "url": "http://localhost:8501/Farm_Tools"},
    {"label": "Marketplace", "icon": "🛒", "url": "http://localhost:8501/Marketplace"},
    {"label": "Crop", "icon": "🌾", "url": "http://localhost:8501/Crop"},
    {"label": "Fertilizer & Orders", "icon": "📦", "url": "http://localhost:8501/Fertilizer_and_Orders"},
    {"label": "Weather", "icon": "🌤", "url": "http://localhost:8501/Weather"},
    {"label": "Community Forum", "icon": "💬", "url": "http://localhost:8501/Community_Forum"},
    {"label": "Expert Consultation", "icon": "🧑‍🌾", "url": "http://localhost:8501/Expert_Consultation"},
    {"label": "Government Schemes", "icon": "🏛", "url": "http://localhost:8501/Government_Schemes"},
    {"label": "News & Market Insights", "icon": "📰", "url": "http://localhost:8501/News_Market_Insights"},
    {"label": "Chatbot", "icon": "🤖", "url": "http://localhost:8501/Chatbot"},
]

# ---------------------- CUSTOM CSS ----------------------
st.markdown(f"""
<style>
.stApp {{
    background: url("data:image/png;base64,{img_base64}") no-repeat center fixed;
    background-size: cover;
}}
.main-title {{
    font-size: 3rem;
    text-align: center;
    font-weight: bold;
    color: white;
    margin-bottom: 30px;
    text-shadow: 2px 2px 6px #000;
}}
.tool-card {{
    background: rgba(0,0,0,0.45);
    border-radius: 18px;
    padding: 25px 20px;
    text-align: center;
    cursor: pointer;
    box-shadow: 0 6px 18px rgba(0,0,0,0.25);
    transition: 0.25s;
}}
.tool-card:hover {{
    transform: translateY(-6px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.35);
}}
.tool-icon {{
    font-size: 3rem;
    margin-bottom: 12px;
}}
.tool-label {{
    font-size: 1.25rem;
    color: white;
    font-weight: 600;
    text-shadow: 1px 1px 3px #000;
}}
a {{
    text-decoration: none;
}}
</style>
""", unsafe_allow_html=True)

# ---------------------- TITLE ----------------------
st.markdown(f"<div class='main-title'>{translations[lang_code]['title']}</div>", unsafe_allow_html=True)

# ---------------------- TOOL GRID ----------------------
for i in range(0, len(tool_options), 3):
    columns = st.columns(3)
    for col, tool in zip(columns, tool_options[i:i+3]):
        with col:
            label = translations[lang_code].get(tool["label"], tool["label"])
            st.markdown(
                f"""
                <a href="{tool['url']}" target="_self">
                    <div class="tool-card">
                        <div class="tool-icon">{tool['icon']}</div>
                        <div class="tool-label">{label}</div>
                    </div>
                </a>
                """,
                unsafe_allow_html=True
            )
            