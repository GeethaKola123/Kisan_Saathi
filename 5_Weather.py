import streamlit as st
import requests
from datetime import datetime

# ---------------- Language Selection ----------------
lang = st.sidebar.selectbox("🌐 Language", ["English", "తెలుగు", "हिंदी"])
lang_key = "en" if lang == "English" else "te" if lang == "తెలుగు" else "hi"

# ---------------- Translations ----------------
translations = {
    "en": {
        "title": "Weather Forecast",
        "subtitle": "Get accurate weather information to plan your farming activities",
        "search_placeholder": "Enter your village/city...",
        "current_weather": "Current Weather",
        "humidity": "Humidity",
        "wind_speed": "Wind Speed",
        "visibility": "Visibility",
        "uv_index": "UV Index",
        "farming_alerts": "Farming Alerts",
        "heavy_rain": "Heavy Rain Expected",
        "heavy_rain_desc": "Heavy rainfall predicted for next 2 days. Consider drainage measures.",
        "optimal_planting": "Optimal Planting Conditions",
        "optimal_planting_desc": "Temperature and humidity levels are ideal for wheat planting.",
        "good_irrigation": "Good Irrigation Weather",
        "good_irrigation_desc": "Low humidity and moderate temperature - perfect for field irrigation.",
        "five_day_forecast": "5-Day Forecast",
        "todays_farming_tips": "Today's Farming Tips",
        "irrigation_advice": "Irrigation Advice",
        "irrigation_advice_desc": "Current humidity is moderate. Ideal time for watering crops early morning or evening.",
        "pest_management": "Pest Management",
        "pest_management_desc": "Warm and humid conditions may increase pest activity. Monitor crops closely.",
        "field_work": "Field Work",
        "field_work_desc": "Good weather for field activities. Consider fertilizer application or weeding.",
        "high": "high",
        "medium": "medium",
        "low": "low",
    },
    "te": {
        "title": "వాతావరణ సూచన",
        "subtitle": "మీ వ్యవసాయ పనులను ప్లాన్ చేయడానికి ఖచ్చితమైన వాతావరణ సమాచారాన్ని పొందండి",
        "search_placeholder": "మీ గ్రామం/నగరం పేరు నమోదు చేయండి...",
        "current_weather": "ప్రస్తుత వాతావరణం",
        "humidity": "తేమ",
        "wind_speed": "గాలి వేగం",
        "visibility": "వీక్షణ",
        "uv_index": "UV సూచిక",
        "farming_alerts": "వ్యవసాయ హెచ్చరికలు",
        "heavy_rain": "భారీ వర్షం అంచనా",
        "heavy_rain_desc": "వచ్చే 2 రోజులకు భారీ వర్షం అంచనా. నీటి పారుదల చర్యలను పరిగణించండి.",
        "optimal_planting": "సరైన నాటడం పరిస్థితులు",
        "optimal_planting_desc": "గోధుమ నాటడానికి ఉష్ణోగ్రత మరియు తేమ స్థాయిలు ఆదర్శంగా ఉన్నాయి.",
        "good_irrigation": "మంచి నీటిపారుదల వాతావరణం",
        "good_irrigation_desc": "తక్కువ తేమ మరియు మితమైన ఉష్ణోగ్రత - పంటల నీటిపారుదలకు ఖచ్చితమైనది.",
        "five_day_forecast": "5-రోజుల సూచన",
        "todays_farming_tips": "ఈరోజు వ్యవసాయ చిట్కాలు",
        "irrigation_advice": "నీటిపారుదల సలహా",
        "irrigation_advice_desc": "ప్రస్తుత తేమ మితంగా ఉంది. ఉదయం లేదా సాయంత్రం పంటలకు నీరు పెట్టడానికి ఇది సరైన సమయం.",
        "pest_management": "తెగుళ్ళ నిర్వహణ",
        "pest_management_desc": "వెచ్చని మరియు తేమతో కూడిన పరిస్థితులు తెగుళ్ళ కార్యకలాపాలను పెంచుతాయి. పంటలను జాగ్రత్తగా పర్యవేక్షించండి.",
        "field_work": "క్షేత్ర పని",
        "field_work_desc": "క్షేత్ర పనులకు మంచి వాతావరణం. ఎరువుల వాడకం లేదా కలుపు తీయడం గురించి ఆలోచించండి.",
        "high": "అధిక",
        "medium": "మధ్యస్థ",
        "low": "తక్కువ",
    },
    "hi": {
        "title": "मौसम का पूर्वानुमान",
        "subtitle": "अपनी कृषि गतिविधियों की योजना बनाने के लिए सटीक मौसम की जानकारी प्राप्त करें",
        "search_placeholder": "अपने गांव/शहर का नाम दर्ज करें...",
        "current_weather": "वर्तमान मौसम",
        "humidity": "आर्द्रता",
        "wind_speed": "हवा की गति",
        "visibility": "दृश्यता",
        "uv_index": "यूवी सूचकांक",
        "farming_alerts": "कृषि अलर्ट",
        "heavy_rain": "भारी बारिश की संभावना",
        "heavy_rain_desc": "अगले 2 दिनों के लिए भारी बारिश का अनुमान है। जल निकासी उपायों पर विचार करें।",
        "optimal_planting": "इष्टतम रोपण स्थितियाँ",
        "optimal_planting_desc": "गेहूं रोपण के लिए तापमान और आर्द्रता का स्तर आदर्श है।",
        "good_irrigation": "अच्छे सिंचाई का मौसम",
        "good_irrigation_desc": "कम आर्द्रता और मध्यम तापमान - खेत की सिंचाई के लिए एकदम सही।",
        "five_day_forecast": "5-दिन का पूर्वानुमान",
        "todays_farming_tips": "आज के कृषि सुझाव",
        "irrigation_advice": "सिंचाई सलाह",
        "irrigation_advice_desc": "वर्तमान आर्द्रता मध्यम है। सुबह या शाम को फसलों को पानी देने का आदर्श समय।",
        "pest_management": "कीट प्रबंधन",
        "pest_management_desc": "गर्म और आर्द्र मौसम से कीटों की गतिविधि बढ़ सकती है। फसलों की बारीकी से निगरानी करें।",
        "field_work": "खेत का काम",
        "field_work_desc": "खेत की गतिविधियों के लिए अच्छा मौसम। उर्वरक लगाने या निराई पर विचार करें।",
        "high": "उच्च",
        "medium": "मध्यम",
        "low": "कम",
    }
}

t = translations[lang_key]

# ---------------- Streamlit Page Config ----------------
st.set_page_config(page_title=t["title"], layout="wide")
st.markdown(f'<h1 style="text-align:center;">{t["title"]}</h1>', unsafe_allow_html=True)
st.markdown(f'<p style="text-align:center;">{t["subtitle"]}</p>', unsafe_allow_html=True)

# ---------------- Custom CSS ----------------
st.markdown("""
<style>
.card { background-color:white; border-radius:10px; box-shadow:0 4px 8px rgba(0,0,0,0.1); padding:20px; margin-bottom:20px; }
.alert-card { padding:15px; border-radius:10px; margin-bottom:15px; line-height:1.4; }
.alert-card.high { background-color:#FEECEB; border-left:5px solid #EB5757; }
.alert-card.medium { background-color:#FEF4E7; border-left:5px solid #F37021; }
.alert-card.low { background-color:#EBF8F0; border-left:5px solid #117A37; }
.alert-label { font-size:0.8em; font-weight:bold; padding:2px 8px; border-radius:12px; width:fit-content; text-transform:uppercase; margin-left:auto; }
.alert-card.high .alert-label { background-color:#EB5757; color:white; }
.alert-card.medium .alert-label { background-color:#F37021; color:white; }
.alert-card.low .alert-label { background-color:#117A37; color:white; }
.forecast-day { text-align:center; flex:1; padding:10px; }
.forecast-temp { font-weight:bold; font-size:1.2em; }
</style>
""", unsafe_allow_html=True)

# ---------------- Input ----------------
city = st.text_input("", placeholder=t["search_placeholder"])
if st.button("🔍"):
    if city:
        API_KEY=your_api_key_here
        # Current weather
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
        forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={API_KEY}"

        weather_res = requests.get(weather_url).json()
        forecast_res = requests.get(forecast_url).json()

        if weather_res.get("cod") == 200:
            # ---------------- Left Column ----------------
            main_col, sidebar_col = st.columns([2,1])
            with main_col:
                st.markdown(f'<div class="card"><h3>📍 {t["current_weather"]} - {city.title()}</h3>', unsafe_allow_html=True)
                col1, col2 = st.columns([1,2])
                with col1:
                    temp = round(weather_res["main"]["temp"])
                    desc = weather_res["weather"][0]["description"].title()
                    st.markdown(f'<h1 style="font-size:3em; color:#117A37;">{temp}°C</h1>', unsafe_allow_html=True)
                    st.markdown(f'<p>{desc}</p>', unsafe_allow_html=True)
                with col2:
                    st.markdown(f"""
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
                        <div>💧 {t["humidity"]}<br><b>{weather_res['main']['humidity']}%</b></div>
                        <div>🌬 {t["wind_speed"]}<br><b>{weather_res['wind']['speed']} km/h</b></div>
                        <div>👁 {t["visibility"]}<br><b>{weather_res.get('visibility',0)/1000} km</b></div>
                        <div>☀ {t["uv_index"]}<br><b>6</b></div>
                    </div>
                    """, unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

                # 5-Day Forecast
                st.markdown(f'<div class="card"><h3>{t["five_day_forecast"]}</h3>', unsafe_allow_html=True)
                forecast_days = {}
                for item in forecast_res["list"]:
                    date_txt = item["dt_txt"].split()[0]
                    if date_txt not in forecast_days:
                        forecast_days[date_txt] = {"temp_min":item["main"]["temp_min"], "temp_max":item["main"]["temp_max"], "desc":item["weather"][0]["main"]}
                forecast_cols = st.columns(5)
                for col, (date, info) in zip(forecast_cols, list(forecast_days.items())[:5]):
                    dt_obj = datetime.strptime(date,"%Y-%m-%d")
                    day_name = dt_obj.strftime("%a")
                    col.markdown(f'<div class="forecast-day"><b>{day_name}</b><br>☀<br><span class="forecast-temp">{round(info["temp_max"])}°</span><br>{round(info["temp_min"])}°<br>{info["desc"]}</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

            # ---------------- Right Column ----------------
        

                # Farming Tips
                st.markdown(f'<div class="card"><h3>🌱 {t["todays_farming_tips"]}</h3>', unsafe_allow_html=True)
                st.markdown(f"""
                    <div class="alert-card low">
                        <b>{t["irrigation_advice"]}</b>
                        <p>{t["irrigation_advice_desc"]}</p>
                    </div>
                    <div class="alert-card medium">
                        <b>{t["pest_management"]}</b>
                        <p>{t["pest_management_desc"]}</p>
                    </div>
                    <div class="alert-card low">
                        <b>{t["field_work"]}</b>
                        <p>{t["field_work_desc"]}</p>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.error("City not found! Please check spelling or try another city.")
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