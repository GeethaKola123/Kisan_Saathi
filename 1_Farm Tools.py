import streamlit as st
import wikipediaapi
from deep_translator import GoogleTranslator

# =====================================================================
# PAGE CONFIG
# =====================================================================

st.set_page_config(page_title="Agro Mitra — Farm Tools", layout="wide")

# =====================================================================
# CSS
# =====================================================================

st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #A8FF78, #78FFD6);
}
.block {
    padding: 20px;
    border-radius: 15px;
    background: rgba(255,255,255,0.85);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# =====================================================================
# LANGUAGE
# =====================================================================

LANG = st.sidebar.selectbox("🌐 Language", ["English", "తెలుగు", "हिंदी"])

lang_map = {"English": "en", "తెలుగు": "te", "हिंदी": "hi"}
lang_code = lang_map[LANG]

# =====================================================================
# HEADER
# =====================================================================

st.title("🌾 Kisan Saathi — Smart Farming Assistant")

# =====================================================================
# 🌱 CROP PREDICTION
# =====================================================================

st.markdown("<div class='block'>", unsafe_allow_html=True)

st.subheader("🌱 Crop Prediction")

col1, col2, col3 = st.columns(3)

with col1:
    rain = st.text_input("Rainfall (mm)")

with col2:
    temp = st.text_input("Temperature (°C)")

with col3:
    hum = st.text_input("Humidity (%)")

if st.button("Predict Crop"):
    try:
        r, t, h = float(rain), float(temp), float(hum)

        if r > 200 and h > 60:
            crop = "Rice"
        elif 50 < r < 150:
            crop = "Cotton"
        elif t < 20:
            crop = "Wheat"
        else:
            crop = "Maize"

        result = f"Recommended Crop: {crop}"

        if lang_code != "en":
            result = GoogleTranslator(source='en', target=lang_code).translate(result)

        st.success(result)

    except:
        st.error("Enter valid numbers")

st.markdown("</div>", unsafe_allow_html=True)

# =====================================================================
# 🧪 FERTILIZER
# =====================================================================

st.markdown("<div class='block'>", unsafe_allow_html=True)

st.subheader("🧪 Fertilizer Suggestion")

ctype = st.text_input("Crop Type")
ph = st.text_input("Soil pH")

if st.button("Get Fertilizer"):
    crop = ctype.lower()

    if crop in ["rice", "paddy"]:
        result = "Use Urea and DAP"
    elif crop == "wheat":
        result = "Use Nitrogen rich fertilizer"
    else:
        result = "Use NPK fertilizer"

    if lang_code != "en":
        result = GoogleTranslator(source='en', target=lang_code).translate(result)

    st.success(result)

st.markdown("</div>", unsafe_allow_html=True)

# =====================================================================
# 🌿 PLANT DICTIONARY (FIXED USER-AGENT)
# =====================================================================

st.markdown("<div class='block'>", unsafe_allow_html=True)

st.subheader("🌿 Plant Dictionary")

plant = st.text_input("Plant Name")

if st.button("Search Plant"):
    if plant:
        try:
            query = plant

            # Translate input to English if needed
            if lang_code != "en":
                query = GoogleTranslator(source='auto', target='en').translate(plant)

            # ✅ FIXED USER-AGENT HERE
            wiki = wikipediaapi.Wikipedia(
                language='en',
                user_agent='AgroMitraApp/1.0 (student project)'
            )

            page = wiki.page(query)

            if page.exists():
                text = page.summary[:50000]

                # Translate back to selected language
                if lang_code != "en":
                    text = GoogleTranslator(source='en', target=lang_code).translate(text)

                st.info(text)

            else:
                st.error("Plant not found")

        except Exception as e:
            st.error(str(e))

st.markdown("</div>", unsafe_allow_html=True)