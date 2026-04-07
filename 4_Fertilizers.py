import streamlit as st
from urllib.parse import urlparse, parse_qs

# ---------------- Global Translations (Navigation) ----------------
translations_nav = {
    "en": {
        "title": "Agro Mitra",
        "home": "Home",
        "farm_tools": "Farm Tools",
        "marketplace": "Marketplace",
        "crops": "Crops",
        "fertilizers": "Fertilizers",
        "weather": "Weather",
        "community": "Community",
        "expert_help": "Expert Help",
        "gov_schemes": "Gov Schemes",
        "news": "News",
        "management": "Management",
        "chatbot": "Chatbot"
    },
    "hi": {
        "title": "एग्रोमित्र",
        "home": "होम",
        "farm_tools": "कृषि उपकरण",
        "marketplace": "बाज़ार",
        "crops": "फसलें",
        "fertilizers": "उर्वरक",
        "weather": "मौसम",
        "community": "समुदाय",
        "expert_help": "विशेषज्ञ सहायता",
        "gov_schemes": "सरकारी योजनाएं",
        "news": "समाचार",
        "management": "प्रबंधन",
        "chatbot": "चैटबॉट"
    },
    "te": {
        "title": "అగ్రోమిత్ర",
        "home": "హోమ్",
        "farm_tools": "వ్యవసాయ ఉపకరణాలు",
        "marketplace": "మార్కెట్",
        "crops": "పంటలు",
        "fertilizers": "ఎరువులు",
        "weather": "వాతావరణం",
        "community": "సమాజం",
        "expert_help": "నిపుణుల సహాయం",
        "gov_schemes": "ప్రభుత్వ పథకాలు",
        "news": "వార్తలు",
        "management": "నిర్వహణ",
        "chatbot": "చాట్‌బాట్"
    }
}

# ---------------- Fertilizer Page Translations ----------------
translations = {
    "en": {
        "title": "Fertilizers & Orders",
        "subtitle": "Compare prices and order fertilizers with voice commands",
        "price_comparison": "Fertilizer Price Comparison",
        "voice_order": "Voice Order",
        "listening": "Listening...",
        "say_something": 'Say something like: "I need 10 bags of Urea and 5 bags of DAP for my wheat field"',
        "start_recording": "Start Recording",
        "stop_recording": "Stop Recording",
        "recent_voice_orders": "Recent Voice Orders:",
        "recommendations": "Recommendations",
        "fertilizer_calculator": "Fertilizer Calculator",
        "crop_type": "Crop type",
        "farm_area": "Farm area (acres)",
        "growth_stage": "Growth stage",
        "calculate": "Calculate Requirements",
        "recommended_for": "Recommended for 5 acres of Wheat:",
        "total_cost": "Total Cost:",
        "market_trends": "Market Trends & Analysis",
        "urea": "Urea",
        "dap": "DAP",
        "potash": "Potash (MOP)",
        "npk": "NPK 10-26-26",
        "in_stock": "In Stock",
        "limited_stock": "Limited Stock",
        "order": "Order",
        "quick_order": "Quick Order",
        "wheat": "Wheat",
        "tomato": "Tomato",
        "tillering": "Tillering",
        "flowering": "Flowering",
        "apply_next_7_days": "Apply: Next 7 days",
        "apply_immediately": "Apply: Immediately",
        "urea_increase": "Urea price increase this month",
        "npk_decrease": "NPK price decrease this week",
        "avg_dap_price": "Average DAP price",
        "stock_availability": "Stock availability",
        "fertilizer": "Fertilizer",
        "quantity": "Quantity",
        "apply": "Apply"
    },
    "te": {
        "title": "ఎరువులు & ఆర్డర్లు",
        "subtitle": "వాయిస్ కమాండ్ ద్వారా ఎరువుల ధరలను పోల్చండి మరియు ఆర్డర్ చేయండి",
        "price_comparison": "ఎరువుల ధర పోలిక",
        "voice_order": "వాయిస్ ఆర్డర్",
        "listening": "వింటుంది...",
        "say_something": '"నా గోధుమ పంటకు 10 బస్తాల యూరియా మరియు 5 బస్తాల DAP కావాలి" అని చెప్పండి',
        "start_recording": "రికార్డింగ్ ప్రారంభించు",
        "stop_recording": "రికార్డింగ్ ఆపు",
        "recent_voice_orders": "ఇటీవలి వాయిస్ ఆర్డర్లు:",
        "recommendations": "సూచనలు",
        "fertilizer_calculator": "ఎరువుల కాలిక్యులేటర్",
        "crop_type": "పంట రకం",
        "farm_area": "వ్యవసాయ ప్రాంతం (ఎకరాలు)",
        "growth_stage": "పెరుగుదల దశ",
        "calculate": "అవసరాలను లెక్కించు",
        "recommended_for": "5 ఎకరాల గోధుమకు సిఫార్సు చేయబడింది:",
        "total_cost": "మొత్తం ఖర్చు:",
        "market_trends": "మార్కెట్ ట్రెండ్స్ & విశ్లేషణ",
        "urea": "యూరియా",
        "dap": "DAP",
        "potash": "పొటాష్ (MOP)",
        "npk": "NPK 10-26-26",
        "in_stock": "స్టాక్ లో ఉంది",
        "limited_stock": "పరిమిత స్టాక్",
        "order": "ఆర్డర్ చేయండి",
        "quick_order": "త్వరిత ఆర్డర్",
        "wheat": "గోధుమ",
        "tomato": "టమోటా",
        "tillering": "పిల్లలు వేసే దశ",
        "flowering": "పూత దశ",
        "apply_next_7_days": "దరఖాస్తు: వచ్చే 7 రోజులు",
        "apply_immediately": "దరఖాస్తు: వెంటనే",
        "urea_increase": "ఈ నెలలో యూరియా ధర పెరిగింది",
        "npk_decrease": "ఈ వారం NPK ధర తగ్గింది",
        "avg_dap_price": "సగటు DAP ధర",
        "stock_availability": "స్టాక్ లభ్యత",
        "fertilizer": "ఎరువు",
        "quantity": "పరిమాణం",
        "apply": "దరఖాస్తు"
    },
    "hi": {
        "title": "उर्वरक और ऑर्डर",
        "subtitle": "वॉयस कमांड से उर्वरकों की कीमतों की तुलना करें और ऑर्डर करें",
        "price_comparison": "उर्वरक मूल्य तुलना",
        "voice_order": "वॉयस ऑर्डर",
        "listening": "सुन रहा है...",
        "say_something": 'कुछ ऐसा कहें: "मुझे अपने गेहूं के खेत के लिए 10 बोरी यूरिया और 5 बोरी DAP चाहिए"',
        "start_recording": "रिकॉर्डिंग शुरू करें",
        "stop_recording": "रिकॉर्डिंग बंद करें",
        "recent_voice_orders": "हाल के वॉयस ऑर्डर:",
        "recommendations": "अनुशंसाएँ",
        "fertilizer_calculator": "उर्वरक कैलकुलेटर",
        "crop_type": "फसल का प्रकार",
        "farm_area": "खेत का क्षेत्रफल (एकड़)",
        "growth_stage": "विकास चरण",
        "calculate": "आवश्यकताओं की गणना करें",
        "recommended_for": "5 एकड़ गेहूं के लिए अनुशंसित:",
        "total_cost": "कुल लागत:",
        "market_trends": "बाजार रुझान और विश्लेषण",
        "urea": "यूरिया",
        "dap": "DAP",
        "potash": "पोटाश (MOP)",
        "npk": "NPK 10-26-26",
        "in_stock": "स्टॉक में",
        "limited_stock": "सीमित स्टॉक",
        "order": "ऑर्डर करें",
        "quick_order": "त्वरित ऑर्डर",
        "wheat": "गेहूं",
        "tomato": "टमाटर",
        "tillering": "कल्ले निकलने का चरण",
        "flowering": "फूल आने का चरण",
        "apply_next_7_days": "लागू करें: अगले 7 दिन",
        "apply_immediately": "लागू करें: तुरंत",
        "urea_increase": "इस महीने यूरिया की कीमत में वृद्धि",
        "npk_decrease": "इस सप्ताह NPK की कीमत में कमी",
        "avg_dap_price": "औसत DAP मूल्य",
        "stock_availability": "स्टॉक उपलब्धता",
        "fertilizer": "उर्वरक",
        "quantity": "मात्रा",
        "apply": "लागू करें"
    }
}

# ---------------- Page Config ----------------
st.set_page_config(page_title="🌱 Agro Mitra - Fertilizers", layout="wide", initial_sidebar_state="collapsed")

# ---------------- Navbar Function ----------------
def nav_bar(current_lang):
    t = translations_nav[current_lang]
    st.markdown(f"""
        <style>
            .nav-container {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 10px 50px;
                background-color: #f7f7f7;
                border-bottom: 1px solid #ddd;
                width: 100%;
                top: 0;
                position: fixed;
                z-index: 100;
            }}
            .logo-text {{ font-size: 1.5em; font-weight: bold; color: #333; }}
            .nav-links {{ display: flex; gap: 25px; }}
            .nav-link a {{ color: #333; text-decoration: none; font-weight: 600; }}
            .nav-link a:hover {{ color: #117A37; }}
            .active-link a {{ background-color: #117A37; color: white; border-radius: 5px; padding: 5px 10px; }}
        </style>
        <div class="nav-container">
            <div class="logo-text">{t['title']}</div>
            <div class="nav-links">
                <div class="nav-link"><a href="/?lang={current_lang}">{t['home']}</a></div>
                <div class="nav-link"><a href="/Marketplace?lang={current_lang}">{t['marketplace']}</a></div>
                <div class="nav-link active-link"><a href="/Fertilizers?lang={current_lang}">{t['fertilizers']}</a></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# ---------------- Language Selector ----------------
st.sidebar.title("🌐 Language")
lang = st.sidebar.selectbox("Select Language", ["English", "తెలుగు", "हिंदी"])
lang_key = "en" if lang == "English" else "te" if lang == "తెలుగు" else "hi"
t = translations[lang_key]

# Navbar
nav_bar(lang_key)

# ---------------- Page Content ----------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.title(t["title"])
st.subheader(t["subtitle"])

# --- Fertilizer Calculator ---
st.header(t["fertilizer_calculator"])
crop = st.selectbox(t["crop_type"], [t["wheat"], t["tomato"]])
area = st.number_input(t["farm_area"], min_value=1, step=1)
stage = st.selectbox(t["growth_stage"], [t["tillering"], t["flowering"]])

if st.button(t["calculate"], use_container_width=True, type="primary"):
    st.success(f"{t['recommended_for']} {area} acres of {crop}")
    st.info(f"• {t['urea']}: 100 kg\n• {t['dap']}: 50 kg\n• {t['potash']}: 30 kg")
    st.write(f"{t['total_cost']} ₹8,500**")

# --- Recommendations ---
st.header(t["recommendations"])
st.info(f"🌱 {t['apply_next_7_days']}: {t['urea']} (50kg/acre)")
st.info(f"🌸 {t['apply_immediately']}: {t['dap']} (25kg/acre)")

# --- Price Comparison ---
st.header(t["price_comparison"])
st.table({
    t["fertilizer"]: [t["urea"], t["dap"], t["potash"], t["npk"]],
    "₹/50kg": [600, 1350, 1200, 1400],
    t["stock_availability"]: [t["in_stock"], t["limited_stock"], t["in_stock"], t["in_stock"]]
})

# --- Market Trends ---
st.header(t["market_trends"])
st.warning(f"📈 {t['urea_increase']}")
st.success(f"📉 {t['npk_decrease']}")
st.info(f"📊 {t['avg_dap_price']}: ₹1350")

# --- Quick Order ---
st.header(t["quick_order"])
col1, col2 = st.columns(2)
with col1:
    fert = st.selectbox(t["fertilizer"], [t["urea"], t["dap"], t["npk"], t["potash"]])
with col2:
    qty = st.number_input(t["quantity"], min_value=1, step=1)

if st.button(t["order"], use_container_width=True, type="primary"):
    st.success(f"✅ {qty} bags of {fert} ordered successfully!")
st.markdown("""
<style>
.ai-button {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #4CAF50;
    color: white;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 28px;
    cursor: pointer;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    z-index: 9999;
}
</style>

<div class="ai-button" onclick="alert('AI Chat Coming Soon 🤖')">
🤖
</div>
""", unsafe_allow_html=True)