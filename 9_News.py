import streamlit as st
import requests
from deep_translator import GoogleTranslator

# --- 1. Configuration ---
NEWS_API_KEY = "9c3b5520e99244a78f2c9b583e16925e"

# --- 2. Enhanced Functions with Caching ---
@st.cache_data(ttl=3600)
def fetch_agri_news(api_key):
    # Using 'top-headlines' for higher quality/verified news
    url = f"https://newsapi.org/v2/everything?q=agriculture+India+farming&sortBy=relevancy&language=en&apiKey={api_key}"
    try:
        response = requests.get(url, timeout=10)
        return response.json().get("articles", [])[:6]
    except:
        return []

@st.cache_data(ttl=3600)
def translate_content(text, target_lang_name):
    lang_map = {"English": "en", "తెలుగు": "te", "हिन्दी": "hi"}
    dest = lang_map.get(target_lang_name, "en")
    if dest == "en" or not text:
        return text
    try:
        return GoogleTranslator(source='auto', target=dest).translate(text)
    except:
        return text

# --- 3. Sidebar Setup ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2942/2942502.png", width=100)
st.sidebar.title("Kisan Saathi Settings")
selected_lang = st.sidebar.selectbox(
    "Preferred Language / భాషను ఎంచుకోండి",
    ("English", "తెలుగు", "हिन्दी")
)
st.session_state.lang = selected_lang

# --- 4. Advanced Professional CSS ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] {{
        font-family: 'Poppins', sans-serif;
    }}

    .main {{
        background-color: #f4f7f6;
    }}

    /* Hero Section */
    .hero-container {{
        background: linear-gradient(135deg, #1b5e20 0%, #43a047 100%);
        padding: 40px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }}

    /* News Card Design */
    .news-card-v2 {{
        background: white;
        border-radius: 20px;
        overflow: hidden;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        height: 100%;
        display: flex;
        flex-direction: column;
    }}

    .news-card-v2:hover {{
        transform: translateY(-10px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.15);
    }}

    .news-img {{
        width: 100%;
        height: 200px;
        object-fit: cover;
    }}

    .news-content {{
        padding: 20px;
        flex-grow: 1;
    }}

    .source-badge {{
        background: #e8f5e9;
        color: #2e7d32;
        padding: 4px 12px;
        border-radius: 50px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 10px;
    }}

    .news-title {{
        font-size: 1.1rem;
        font-weight: 600;
        color: #1a1a1a;
        margin-bottom: 10px;
        line-height: 1.4;
    }}

    .news-desc {{
        font-size: 0.9rem;
        color: #666;
        margin-bottom: 15px;
    }}

    .btn-link {{
        color: white;
        background: #2e7d32;
        padding: 10px 20px;
        border-radius: 10px;
        text-decoration: none;
        font-size: 14px;
        font-weight: 600;
        display: inline-block;
        transition: background 0.3s;
    }}

    .btn-link:hover {{
        background: #1b5e20;
    }}
    </style>
""", unsafe_allow_html=True)

# --- 5. App Layout ---

# Hero Banner
hero_title = translate_content("Farmer's Intelligence Hub", selected_lang)
hero_sub = translate_content("Stay ahead with real-time agricultural insights across India.", selected_lang)

st.markdown(f"""
    <div class="hero-container">
        <h1>🌱 {hero_title}</h1>
        <p>{hero_sub}</p>
    </div>
""", unsafe_allow_html=True)

# Fetch Articles
articles = fetch_agri_news(NEWS_API_KEY)

if articles:
    # Use 3 columns for a clean, modern grid
    cols = st.columns(3)
    
    for idx, art in enumerate(articles):
        with cols[idx % 3]:
            # Translation with spinner only on interaction
            with st.spinner('Translating...'):
                t_title = translate_content(art.get('title', ''), selected_lang)
                t_desc = translate_content(art.get('description', '')[:100], selected_lang)
                btn_text = translate_content("Read Full News", selected_lang)
            
            # Use article image if available, else a placeholder
            img_url = art.get('urlToImage') or "https://images.unsplash.com/photo-1500382017468-9049fed747ef?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80"
            
            st.markdown(f"""
                <div class="news-card-v2">
                    <img src="{img_url}" class="news-img">
                    <div class="news-content">
                        <span class="source-badge">{art['source']['name']}</span>
                        <div class="news-title">{t_title}</div>
                        <div class="news-desc">{t_desc}...</div>
                        <a href="{art['url']}" target="_blank" class="btn-link">{btn_text}</a>
                    </div>
                </div>
            """, unsafe_allow_html=True)
else:
    st.info("No fresh news updates at the moment. Check back soon!")