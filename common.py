import streamlit as st
import os

# --- Multilingual Text Data ---
translations = {
    "en": {
        "nav_home": "Home",
        "nav_tools": "Farm Tools",
        "nav_market": "Marketplace",
        "nav_crops": "Crops",
        "nav_fertilizers": "Fertilizers",
        "nav_weather": "Weather",
        "nav_community": "Community",
        "nav_expert": "Expert Help",
        "nav_gov": "Gov Schemes",
        "nav_news": "News",
        "nav_mgmt": "Management",
        "nav_chat": "Chatbot",
        "tagline": "Empowering farmers with technology, community, and expert guidance",
        "get_started": "Get Started",
        "join_community": "Join Community",
    },
    "te": {
        "nav_home": "హోమ్",
        "nav_tools": "పంట పరికరాలు",
        "nav_market": "మార్కెట్‌ప్లేస్",
        "nav_crops": "పంటలు",
        "nav_fertilizers": "ఎరువులు",
        "nav_weather": "వాతావరణం",
        "nav_community": "సంఘం",
        "nav_expert": "నిపుణుల సహాయం",
        "nav_gov": "ప్రభుత్వ పథకాలు",
        "nav_news": "వార్తలు",
        "nav_mgmt": "నిర్వహణ",
        "nav_chat": "చాట్‌బాట్",
        "tagline": "సాంకేతికత, సంఘం, మరియు నిపుణుల మార్గదర్శకత్వంతో రైతులను శక్తివంతం చేయడం",
        "get_started": "ప్రారంభించండి",
        "join_community": "సంఘంలో చేరండి",
    },
    "hi": {
        "nav_home": "होम",
        "nav_tools": "कृषि उपकरण",
        "nav_market": "मार्केटप्लेस",
        "nav_crops": "फसलें",
        "nav_fertilizers": "उर्वरक",
        "nav_weather": "मौसम",
        "nav_community": "समुदाय",
        "nav_expert": "विशेषज्ञ सहायता",
        "nav_gov": "सरकारी योजनाएं",
        "nav_news": "समाचार",
        "nav_mgmt": "प्रबंधन",
        "nav_chat": "चैटबॉट",
        "tagline": "प्रौद्योगिकी, समुदाय और विशेषज्ञ मार्गदर्शन से किसानों को सशक्त बनाना",
        "get_started": "शुरू करें",
        "join_community": "समुदाय में शामिल हों",
    },
}

def load_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Error: The file '{file_name}' was not found.")

def nav_bar(current_page):
    load_css("style.css")
    
    t = translations[st.session_state.lang]

    st.markdown(
        f"""
        <div class="top-nav-bar">
            <div class="logo">
                <img src="https://i.ibb.co/6y4b03r/kisan-saathi-logo.png" width="40" style="vertical-align: middle;">
                <span class="logo-text">Kisan Saathi</span>
            </div>
            <div class="nav-links">
                <a href="Home" class="nav-link {'active' if current_page == 'Home' else ''}">{t['nav_home']}</a>
                <a href="Marketplace" class="nav-link {'active' if current_page == 'Marketplace' else ''}">{t['nav_market']}</a>
                <a href="Farm_Tools" class="nav-link {'active' if current_page == 'Farm_Tools' else ''}">{t['nav_tools']}</a>
                <a href="Crops" class="nav-link {'active' if current_page == 'Crops' else ''}">{t['nav_crops']}</a>
                <a href="Fertilizers" class="nav-link {'active' if current_page == 'Fertilizers' else ''}">{t['nav_fertilizers']}</a>
                <a href="Weather" class="nav-link {'active' if current_page == 'Weather' else ''}">{t['nav_weather']}</a>
                <a href="Community" class="nav-link {'active' if current_page == 'Community' else ''}">{t['nav_community']}</a>
                <a href="Expert_Help" class="nav-link {'active' if current_page == 'Expert_Help' else ''}">{t['nav_expert']}</a>
                <a href="Gov_Schemes" class="nav-link {'active' if current_page == 'Gov_Schemes' else ''}">{t['nav_gov']}</a>
                <a href="News" class="nav-link {'active' if current_page == 'News' else ''}">{t['nav_news']}</a>
                <a href="Management" class="nav-link {'active' if current_page == 'Management' else ''}">{t['nav_mgmt']}</a>
                <a href="Chatbot" class="nav-link {'active' if current_page == 'Chatbot' else ''}">{t['nav_chat']}</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True) # Spacer