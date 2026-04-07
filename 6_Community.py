import streamlit as st
import json
import os
from datetime import datetime

# --- 1. Page Config & CSS ---
st.set_page_config(page_title="Kisan Saathi Choupal", layout="wide")

st.markdown("""
<style>
    [data-testid="stAppViewContainer"] { background-color: #f0f2f0; }
    
    .choupal-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 6px solid #2e7d32;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    
    .card-header { font-size: 0.85rem; color: #666; display: flex; justify-content: space-between; }
    .card-title { color: #1b5e20; font-size: 1.2rem; font-weight: bold; margin-top: 10px; }
    .card-category { background: #e8f5e9; color: #2e7d32; padding: 2px 10px; border-radius: 20px; font-size: 0.75rem; font-weight: bold; }
    
    .stTextInput>div>div>input { border-radius: 10px; }
    .stButton>button { border-radius: 20px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- 2. Language ---
lang = st.sidebar.selectbox("🌐 Select Language", ["English", "తెలుగు", "हिंदी"])

t = {
    "English": {"header": "Community Forum", "ask": "Ask a Question", "loc": "Location", "cat": "Category", "btn": "Post to Choupal"},
    "తెలుగు": {"header": "సమాజ వేదిక", "ask": "ప్రశ్న అడగండి", "loc": "ప్రాంతం", "cat": "వర్గం", "btn": "చౌపల్‌లో పోస్ట్ చేయండి"},
    "हिंदी": {"header": "सामुदायिक मंच", "ask": "प्रश्न पूछें", "loc": "स्थान", "cat": "श्रेणी", "btn": "चौपाल पर पोस्ट करें"}
}[lang]

# --- 3. Data Persistence ---
DATA_FILE = "forum_posts.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

def load_posts():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_posts(posts):
    with open(DATA_FILE, "w") as f:
        json.dump(posts, f, indent=4)

# --- 4. UI Layout ---
st.title(f"🌱 {t['header']}")

# --- New Post Section ---
with st.container():
    col1, col2 = st.columns([2, 1])

    with col1:
        u_name = st.text_input("👤 Name", value="Farmer Saathi")
        content = st.text_area(t['ask'], placeholder="Type your farming query here...")

    with col2:
        u_loc = st.text_input(f"📍 {t['loc']}", placeholder="e.g. Kakinada, AP")
        u_cat = st.selectbox(t['cat'], ["Crop Protection", "Organic Farming", "Government Subsidies", "Market Trends"])

        if st.button(t['btn'], use_container_width=True, type="primary"):
            if content and u_loc:
                posts = load_posts()

                new_post = {
                    "id": len(posts) + 1,
                    "author": u_name,
                    "location": u_loc,
                    "category": u_cat,
                    "text": content,
                    "likes": 0,
                    "date": datetime.now().strftime("%d %b, %Y")
                }

                posts.append(new_post)
                save_posts(posts)

                st.success("✅ Successfully posted!")
                st.rerun()
            else:
                st.error("Please fill all fields")

st.divider()

# --- 5. Display Posts ---
posts = load_posts()

for post in reversed(posts):
    st.markdown(f"""
        <div class="choupal-card">
            <div class="card-header">
                <span>👤 <b>{post['author']}</b> • 📍 {post['location']}</span>
                <span class="card-category">{post['category']}</span>
            </div>
            <div class="card-title">{post['text']}</div>
            <hr style="margin: 15px 0; border: 0.5px solid #eee;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-size: 0.9rem; color: #2e7d32;">👍 {post['likes']} Farmers helped</span>
                <small style="color: #999;">{post['date']}</small>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Like Button
    if st.button(f"Helpful 👍", key=f"like_{post['id']}"):
        all_posts = load_posts()
        for p in all_posts:
            if p['id'] == post['id']:
                p['likes'] += 1
        save_posts(all_posts)
        st.rerun()