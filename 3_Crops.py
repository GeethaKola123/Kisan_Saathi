import streamlit as st
from urllib.parse import urlparse, parse_qs

# Language translations
translations = {
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

# --- Check and set initial language ---
def get_lang():
    query_params = st.query_params
    if "lang" in query_params:
        st.session_state.lang = query_params["lang"][0]
    elif "lang" not in st.session_state:
        st.session_state.lang = "en"
    return st.session_state.lang

# --- Page config ---
st.set_page_config(page_title="Agro Mitra", layout="wide")

# --- CSS styling to match screenshot colors / buttons ---
st.markdown("""
<style>
body { background-color: #ffffff; }
.navbar {
    background-color: #ffffff;
    padding: 12px 18px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #e6e6e6;
}
.navbar-title { font-size:22px; font-weight:700; color:#1B5E20; }
.nav-links a { margin: 0 10px; color:#333333; text-decoration:none; font-weight:600; }
.nav-links a.active { color:#F57C00; border-bottom:2px solid #F57C00; padding-bottom:3px; }
.view-button {
    background-color: #1976D2;
    color: #ffffff !important;
    padding: 7px 12px;
    border-radius: 6px;
    display:inline-block;
    text-decoration:none;
    font-weight:600;
}
.card {
    border:1px solid #eaeaea;
    border-radius:8px;
    padding:14px;
    margin-bottom:14px;
    background:#ffffff;
    box-shadow: 0 1px 2px rgba(0,0,0,0.03);
}
.badge {
    background: #F57C00;
    color: #fff;
    padding:4px 8px;
    border-radius:6px;
    font-size:12px;
    display:inline-block;
    margin-bottom:8px;
}
.crop-title { color:#1a3c34; margin-bottom:6px; font-weight:700; }
.small { font-size:13px; color:#444444; }
</style>
""", unsafe_allow_html=True)

# --- Translations and detailed guides for 12 crops (en/hi/te) ---
translations = {
    "en": {
        # UI
        "title": "🌱 Agro Mitra",
        "nav": ["Home","Farm Tools","Marketplace","Crops","Fertilizers","Weather","Community","Expert Help","Gov Schemes","News","Management","Chatbot"],
        "seasonal_crops": "Seasonal Crops",
        "subtitle": "Discover the best crops to grow in each season with detailed cultivation guides",
        "summer": "Summer", "monsoon": "Monsoon", "winter": "Winter", "spring": "Spring",
        "view_detailed": "View Detailed Guide",
        "expected_yield": "Expected Yield:",
        "days_badge": "Days",
    },
    "hi": {
        "title": "🌱 एग्रोमित्र",
        "nav": ["होम","खेती उपकरण","बाजार","फसलें","उर्वरक","मौसम","समुदाय","विशेषज्ञ सहायता","सरकारी योजनाएँ","समाचार","प्रबंधन","चैटबॉट"],
        "seasonal_crops": "मौसमी फसलें",
        "subtitle": "विस्तृत खेती मार्गदर्शिकाओं के साथ हर मौसम में उपयुक्त फसलों की जानकारी",
        "summer": "गर्मी", "monsoon": "मानसून", "winter": "सर्दी", "spring": "बसंत",
        "view_detailed": "विस्तृत मार्गदर्शिका देखें",
        "expected_yield": "अपेक्षित उत्पादन:",
        "days_badge": "दिन",
    },
    "te": {
        "title": "🌱 అగ్రోమిత్ర",
        "nav": ["హోమ్","వ్యవసాయ పరికరాలు","మార్కెట్‌ప్లేస్","పంటలు","ఎరువులు","వాతావరణం","సమాజం","నిపుణుల సహాయం","ప్రభుత్వ పథకాలు","వార్తలు","నిర్వహణ","చాట్‌బాట్"],
        "seasonal_crops": "ఋతువారీ పంటలు",
        "subtitle": "వివరమైన సాగు మార్గదర్శకాలతో ప్రతి ఋతువుకు తగిన పంటలు తెలుసుకోండి",
        "summer": "గ్రీష్మం", "monsoon": "వర్షాకాలం", "winter": "శీతాకాలం", "spring": "వసంతం",
        "view_detailed": "వివరమైన గైడ్ చూడండి",
        "expected_yield": "అంచనా దిగుబడి:",
        "days_badge": "రోజులు",
    }
}

# Detailed guides text per crop in 3 languages
detailed_guides = {
    "tomato": {
        "en": """### Tomato — Detailed Guide

**Climate & Soil:** 20–30°C ideal. Sandy loam with pH 6.0–7.0; good drainage.

**Land preparation:** Deep ploughing, add well-decomposed FYM (10–15 t/ha).

**Nursery & Sowing:** Raise seedlings in nursery (25–30 days). Transplant spacing 45x45 cm.

**Fertilizer:** Basal: FYM + 60% P and K; topdress N in 2–3 splits (approx. NPK 100:50:50 kg/ha).

**Irrigation:** Drip irrigation preferred; irrigate every 5–7 days depending on weather.

**Pests & Diseases:** Manage aphids, fruit borer (Pheromone traps/biopesticides). For blight use resistant varieties and appropriate fungicides.

**Harvesting:** Start at 75–90 days; harvest repeatedly every 3–5 days as fruits ripen.
""",
        "hi": """### टमाटर — विस्तृत मार्गदर्शिका

**जलवायु व मिट्टी:** 20–30°C उपयुक्त। दोमट मिट्टी pH 6.0–7.0, अच्छी ड्रेनेज आवश्यक।

**भूमि तैयारी:** गहरी जुताई, 10–15 टन/हैक्टेयर सड़ी हुई गोबर की खाद डालें।

**नर्सरी व बुवाई:** नर्सरी में 25–30 दिवस पोधे तैयार करें। रोपाई पर दूरी 45x45 सेमी।

**उर्वरक:** NPK लगभग 100:50:50 kg/ha; N को 2–3 हिस्सों में दें; बेसल में FYM जोड़ें।

**सिंचाई:** ड्रिप सिंचाई श्रेष्ठ; मौसम के अनुसार हर 5–7 दिन में सिंचाई।

**कीट व रोग:** एफिड्स, फ्रूट बॉरर के लिए फ़ेरोमोन ट्रैप/बायोफफेट्स; ब्लाइट के लिए प्रतिरोधी किस्में व कवकनाशी का उपयोग।

**हार्वेस्ट:** 75–90 दिन में पहली कटाई; 3–5 दिन के अंतराल पर फल तोड़ते रहें।
""",
        "te": """### టమోటా — వివరమైన గైడ్

**వాతావరణం & మట్టి:** 20–30°C అనుకూలం. ఇసుక లోమి మట్టిలో pH 6.0–7.0, మంచి డ్రెయిన్ కావాలి.

**భూమి సిద్ధం:** లోతయిన దిగి, 10–15 టన్/హెక్టారుకు గడ్డి/ఎరువు చేర్చండి.

**నర్సరీ & విత్తనం:** నర్సరీలో 25–30 రోజుల మొక్కలు తయారు చేస్తారు. నాటే దూరం 45x45 సెం.మీ.

**ఎరువుల వినియోగం:** సుమారు NPK 100:50:50kg/ha; N‌ను 2–3 భాగాలుగా ఇవ్వాలి; బేసిక్‌గా FYM పెట్టండి.

**నీరుపారుదల:** డ్రిప్ ఇరిగేషన్ మంచిది; ప్రతి 5–7 రోజులకు నీరు పెట్టండి (వాతావరణం ఆధారంగా).

**పురుగులు & రోగాలు:** ఆఫిడ్స్, ఫ్రూట్ బోరర్‌కి ఫెరోమోన్ ట్రాప్స్/బయోపెస్టిసైడ్స్ వాడండి; బ్లైట్ నివారణకు నిరోధక రకాల విత్తనాలు తీసుకోండి.

**కోత:** 75–90 రోజుల్లో మొదటి కోత; ప్రతి 3–5 రోజులకు ఫలాలను తీయండి.
"""
    },

    "cucumber": {
        "en": """### Cucumber — Detailed Guide

**Climate & Soil:** Warm climate; well-drained fertile soil.

**Sowing:** Direct sowing or transplants; spacing 60x30 cm for vine types.

**Fertilizer:** Apply FYM + NPK as per soil test (approx. 40:60:40 kg/ha).

**Irrigation:** Frequent light irrigation; avoid water stress.

**Pests & Diseases:** Watch for powdery mildew and aphids. Use preventive sprays and good air circulation.

**Harvest:** 45–70 days depending on variety; pick regularly to encourage production.
""",
        "hi": """### खीरा — विस्तृत मार्गदर्शिका

**जलवायु व मिट्टी:** गर्म मौसम व निकास अच्छी मिट्टी उपयुक्त।

**बुवाई:** सीधे बोएं या प्रत्यारोपण करें; स्पेसिंग 60x30 सेमी।

**उर्वरक:** FYM के साथ NPK; मिट्टी परीक्षण के अनुसार मात्राएँ दें।

**सिंचाई:** हल्की और बार-बार सिंचाई; पानी की कमी न होने दें।

**कीट व रोग:** पाउडरी मिल्ड्यू, एफिड्स पर नजर रखें; हवादार रोपण करें।

**कटाई:** किस्म पर निर्भर, 45–70 दिनों में; नियमित कटाई करें।
""",
        "te": """### దోసకాయ — వివరమైన గైడ్

**వాతావరణం & నేల:** వేడి వాతావరణం, మంచి డ్రైనేజ్ నేల అవసరం.

**విత్తనం:** నేరుగా విత్తడం లేదా రొపಣೆ; స్పేసింగ్ 60x30 సెం.మీ.

**ఎరువుల వినియోగం:** FYM తో సహా NPK పట్టణం (మట్టి పరీక్ష ఆధారంగా).

**నీరు:** తరచుగా తక్కువ నీరు ఇవ్వాలి; నీటి లోపం నివారించాలి.

**పురుగులు & రోగాలు:** పౌడరీ మిల్డ్యూ, ఆఫిడ్స్ పై నియంత్రణ చేయాలి; గాలిముట్టు ఉండేలా ఉంచండి.

**కాయలు కోట్టి:** 45–70 రోజుల్లో కోతలు; తరచుగా కోసుకొనండి.
"""
    },

    "okra": {
        "en": """### Okra — Detailed Guide

**Climate & Soil:** Warm-season crop; tolerates heat. Light to medium soils.

**Sowing:** Direct sowing in rows; spacing 30x30 to 60x60 cm depending on variety.

**Fertilizer:** Moderate NPK; FYM recommended.

**Irrigation:** Moderate; avoid waterlogging.

**Pests & Diseases:** Jassids and shoot borers — monitor and use biocontrol where possible.

**Harvest:** 50–90 days; harvest pods frequently (every 2–3 days).
""",
        "hi": """### भिंडी — विस्तृत मार्गदर्शिका

**जलवायु व मिट्टी:** गर्मी सहन करने वाली फसल; हल्की से मध्यम मिट्टी।

**बुवाई:** पंक्तियों में सीधे बोएं; दूरी 30x30 या 60x60 सेमी।

**उर्वरक:** मध्यम NPK; FYM उपयोगी।

**सिंचाई:** मध्यम मात्रा में; जलभरण से बचें।

**कीट व रोग:** जैसिड, शूट बोरर — निगरानी व जैविक नियंत्रण।

**कटाई:** 50–90 दिनों में; फलों को हर 2–3 दिन में तोड़ें।
""",
        "te": """### బెండకాయ — వివరమైన గైడ్

**వాతావరణం & నేల:** వేడి వాతావరణాన్ని తట్టుకునే పంట; లైట్/మీడియం మట్టి మంచిది.

**విత్తనం:** వరుసల్లో నేరుగా విత్తండి; స్పేసింగ్ 30x30 లేదా 60x60 సెం.మీ.

**ఎరువు:** సగటు NPK; FYM ఇవ్వాలి.

**నీరు:** మిధ్యమంగా నీరు; నీరు నిలవకుండా చూడండి.

**పురుగులు & రోగాలు:** జాసిడ్స్, బోరర్‌లపై నియంత్రణ వాడండి.

**పంట కోత:** 50–90 రోజుల్లో; ప్రతి 2–3 రోజులకు కోయండి.
"""
    },

    "rice": {
        "en": """### Rice — Detailed Guide

**Climate & Soil:** Wetland crop; heavy clay soils with puddling preferred.

**Nursery & Transplanting:** Raise seedlings 20–30 days then transplant at 20x15 cm spacing.

**Water management:** Maintain 2–5 cm standing water during tillering & vegetative stages.

**Fertilizer:** Balanced NPK; micronutrients as required.

**Pests & Diseases:** Stem borer, blast — use integrated pest management.

**Harvest:** 120–150 days depending on variety.
""",
        "hi": """### धान — विस्तृत मार्गदर्शिका

**जलवायु व मिट्टी:** पानी वाली जमीन; भारी चिल्लो मिट्टी उपयुक्त।

**नर्सरी व प्रत्यारोपण:** 20–30 दिन की नर्सरी, फिर 20x15 सेमी पर रोपण।

**जल प्रबंधन:** तिल्लर व वनस्पति अवस्थाओं में 2–5 सेमी पानी बनाए रखें।

**उर्वरक:** संतुलित NPK; आवश्यक सूक्ष्म पोषक दें।

**कीट व रोग:** स्टेम बॉरर, ब्लास्ट— एकीकृत प्रबंधन अपनाएँ।

**कटाई:** 120–150 दिनों में कटाई।
""",
        "te": """### వరి — వివరమైన గైడ్

**వాతావరణం & నేల:** నీరు నిలిచే నేలలో మంచి దిగుబడి; క్లే మట్టి అనుకూలం.

**నర్సరీ & నాటకము:** 20–30 రోజుల నర్సరీ తరువాత 20x15 సెం.మీ దూరంలో నాటాలి.

**నీటిపారుదల:** తిల్లరింగ్ లో మరియు వృద్ధి దశలో 2–5 సెం.మీ నీరు నిలవాలి.

**ఎరువులు:** సమతుల్య NPK; సూక్ష్మ పోషకాలు అవసరమైతే ఇవ్వండి.

**పురుగులు & రోగాలు:** స్టెమ్ బోరర్, బ్లాస్ట్ పట్ల జాగ్రత్త.

**కోత:** 120–150 రోజుల్లో కోత.
"""
    },

    "maize": {
        "en": """### Maize — Detailed Guide

**Climate & Soil:** Warm season; well-drained fertile soils.

**Sowing:** Row sowing; spacing 60x20–25 cm.

**Fertilizer:** Apply NPK as per recommended dose (N split applications).

**Irrigation:** Regular, avoid waterlogging.

**Pests & Diseases:** Fall armyworm, stem borers — monitor early.

**Harvest:** 90–110 days; harvest when kernels are mature.
""",
        "hi": """### मक्का — विस्तृत मार्गदर्शिका

**जलवायु व मिट्टी:** गर्म मौसम में उपयुक्त; अच्छी निकास वाली उर्वरक मिट्टी।

**बुवाई:** पंक्ति में बोईं; दूरी 60x20–25 सेमी।

**उर्वरक:** अनुशंसित NPK मात्रा; N को विभाजित दें।

**सिंचाई:** नियमित पर जलभर से बचें।

**कीट व रोग:** फॉल आर्मीवर्म, स्टेम बोरर पर जल्दी निगरानी।

**कटाई:** 90–110 दिनों में; जब दाने पक जाएं तब काटें।
""",
        "te": """### మొక్కజొన్న — వివరమైన గైడ్

**వాతావరణం & పేరు:** వేడి ఆకలి; మంచి డ్రైనేజ్ నేల అవసరం.

**విత్తి విధానం:** వరుసలలో విత్తండి; స్పేసింగ్ 60x20–25 సెం.మీ.

**ఎరువులు:** సూచించిన NPK మేరకు; N‌ను భాగాలుగా ఇవ్వండి.

**నీరు:** రెగ్యులర్ నీరు; నీరు నిల్చకూడదు.

**పురుగులు & రోగాలు:** ఫాల్ ఆర్మీవార్మ్, స్టెమ్ బోరర్‌పై శ్రద్ధ.

**కబురు:** 90–110 రోజుల్లో కోత.
"""
    },

    "cotton": {
        "en": """### Cotton — Detailed Guide

**Climate & Soil:** Warm climate; deep well-drained black soils preferred.

**Sowing:** After first monsoon showers; spacing 90x60 cm or as per variety.

**Fertilizer:** Balanced NPK, soil test based; FYM recommended.

**Irrigation:** Supplementary irrigation during boll formation.

**Pests & Diseases:** Bollworms and sucking pests — use integrated pest management.

**Harvest:** 150–200 days depending on variety and season.
""",
        "hi": """### कपास — विस्तृत मार्गदर्शिका

**जलवायु व मिट्टी:** गर्म मौसम; गहरी काली मिट्टी उपयुक्त।

**बुवाई:** मानसून के बाद या पहली बारिश के बाद; दूरी 90x60 सेमी।

**उर्वरक:** संतुलित NPK; मिट्टी परीक्षण के अनुसार।

**सिंचाई:** बॉल बनने के समय सहायक सिंचाई।

**कीट व रोग:** बोलवर्म्स, चूसने वाले कीट— IPM अपनाएं।

**कटाई:** 150–200 दिनों में।
""",
        "te": """### పత్తి — వివరమైన గైడ్

**వాతావరణం & మట్టి:** వెచ్చని వాతావరణం; లోతైన బ్లాక్ సాయిల్ అనుకూలం.

**విత్తనం:** మొదటి వర్షాల తర్వాత విత్తండి; స్పేసింగ్ 90x60 సెం.మీ.

**ఎరువు:** సమతుల్య NPK; మట్టి పరీక్ష ఆధారంగా.

**నీరు:** బాల్ ఏర్పాటులో సహాయక ఇరిగేషన్.

**పురుగులు:** బోర్లు, చీలికలపై IPM అవసరం.

**కోత:** 150–200 రోజుల్లో.
"""
    },

    "wheat": {
        "en": """### Wheat — Detailed Guide

**Climate & Soil:** Cool season; loam soils best.

**Sowing:** Early winter sowing; row sowing or broadcasting as per region.

**Fertilizer:** Apply N and P as per recommendations; topdress N at tillering.

**Irrigation:** Apply at critical stages — crown root initiation, flowering.

**Pests & Diseases:** Rusts and aphids — monitor and control.

**Harvest:** 120–150 days.
""",
        "hi": """### गेहूं — विस्तृत मार्गदर्शिका

**जलवायु व मिट्टी:** ठंडी ऋतु अनुकूल; दोमट मिट्टी उत्तम।

**बुवाई:** शीतकाल की शुरुआत में; क्षेत्रानुसार पंक्ति या प्रसारण विधि।

**उर्वरक:** N व P दे; टिलरिंग में N का टॉपड्रेस।

**सिंचाई:** क्रिटिकल स्टेज पर सिंचाई (फूल आने तक)।

**कीट व रोग:** रस्ट, एफिड्स— निगरानी व नियंत्रण।

**कटाई:** 120–150 दिनों में।
""",
        "te": """### గోధుమలు — వివరమైన గైడ్

**వాతావరణం & నేల:** చల్లని కాలం సరిపోతుంది; లోమి నేల మంచిది.

**విత్తనం:** శీతాకాల ప్రారంభంలో విత్తండి.

**ఎరువులు:** N,P సూచన మేరకు; టిల్లరింగ్ సమయంలో N ను ఇవ్వండి.

**నీరు:** కీలక దశల్లో నీరు ఇవ్వాలి (బుట్టల ఏర్పాటుకి, పుష్పణ వరకు).

**పురుగులు & రోగాలు:** రస్ట్లు, ఆఫిడ్స్‌పై జాగ్రత్త.

**కోత:** 120–150 రోజుల్లో.
"""
    },

    "mustard": {
        "en": """### Mustard — Detailed Guide

**Climate & Soil:** Cool season oilseed; light soils acceptable.

**Sowing:** Broad or row sowing in early winter.

**Fertilizer:** Moderate NPK; sulfur beneficial.

**Irrigation:** Light irrigation; avoid waterlogging.

**Pests & Diseases:** Aphids and white rust – scouting recommended.

**Harvest:** 90–120 days when pods turn yellow.
""",
        "hi": """### सरसों — विस्तृत मार्गदर्शिका

**जलवायु व मिट्टी:** ठंडे मौसम में तेल फसल; हल्की मिट्टी उपयुक्त।

**बुवाई:** शीतकाल की शुरुआत में।

**उर्वरक:** मध्यम NPK; सल्फर उपयोगी।

**सिंचाई:** हल्की सिंचाई; जलभर से बचें।

**कीट व रोग:** एफिड्स, व्हाइट रस्ट— निगरानी आवश्यक।

**कटाई:** 90–120 दिनों में जब फली पीली हो।
""",
        "te": """### ఆవాలు — వివరమైన గైడ్

**వాతావరణం & నేల:** చల్లటి కాలంలో నూనె గింజల పంట; లైట్ మట్టిలో సాగుతుంది.

**విత్తనం:** శీతాకాల ప్రారంభంలో విత్తండి.

**ఎరువులు:** మధ్యమ NPK; గంధకం (sulfur) ఉపయోగిస్తే మంచిది.

**నీరు:** తేలికపాటి నీరు; నీరు నిలవకూడదు.

**పురుగులు:** ఆఫిడ్స్, వైట్ రస్ట్‌పై జాగ్రత్త.

**కోత:** 90–120 రోజుల్లో, ఫల్లు పసుపుగా మారినప్పుడు.
"""
    },

    "pea": {
        "en": """### Pea — Detailed Guide

**Climate & Soil:** Cool season; prefers well-drained loam.

**Sowing:** Early winter sowing for most regions; row spacing 20–30 cm.

**Fertilizer:** Low N; rhizobium helps N-fixation.

**Irrigation:** Regular, keep soil moist during flowering and pod formation.

**Harvest:** 60–90 days; harvest green pods for vegetable use.
""",
        "hi": """### मटर — विस्तृत मार्गदर्शिका

**जलवायु व मिट्टी:** ठंडी मौसम की फसल; अच्छी निकास वाली दोमट मिट्टी।

**बुवाई:** प्रारंभिक शीतकाल में; पंक्ति दूरी 20–30 सेमी।

**उर्वरक:** कम N; राइजोबियम से N-फिक्सेशन मदद मिलती है।

**सिंचाई:** फूल व फली बनने पर मिट्टी नम रखें।

**कटाई:** 60–90 दिनों में; हरी फली के रूप में काटें।
""",
        "te": """### బాటానీ (Pea) — వివరమైన గైడ్

**వాతావరణం & నేల:** చల్లని కాలంలో పండుతుంది; మంచి డ్రెయిన్ లోం నేల ఇష్టం.

**విత్తనం:** శీతాకాల ప్రారంభంలో; వరుసల మధ్య 20–30 సెం.మీ.

**ఎరువు:** తక్కువ N; రైజోబియం వల్ల N ఫిక్సేషన్ సహాయం.

**నీరు:** పుష్పణ, ఫల ఏర్పాటులో నేల పొడి కాదని చూడండి.

**కోత:** 60–90 రోజుల్లో; పచ్చి పొట్లుగా కోసుకుంటారు.
"""
    },

    "carrot": {
        "en": """### Carrot — Detailed Guide

**Climate & Soil:** Cool-season root crop; sandy loam best.

**Sowing:** Direct sow, thin seedlings to proper spacing.

**Fertilizer:** Moderate N; avoid heavy manure that causes forked roots.

**Irrigation:** Regular, keep soil moist for good root development.

**Pests & Diseases:** Root fly — use appropriate traps and crop hygiene.

**Harvest:** 70–100 days depending on variety.
""",
        "hi": """### गाजर — विस्तृत मार्गदर्शिका

**जलवायु व मिट्टी:** ठंडा मौसम; रेतीली दोमट मिट्टी उत्तम।

**बुवाई:** सीधे बोईं, पौधों को पतला करें।

**उर्वरक:** मध्यम N; अधिक सड़ी हुई खाद से जड़ें विभक्त हो सकती हैं।

**सिंचाई:** नियमित; जड़ों के विकास के लिए मिट्टी नम रखें।

**कीट व रोग:** रूट फ़्लाई के लिए जाल/स्वच्छता।

**कटाई:** 70–100 दिनों में।
""",
        "te": """### గాజర — వివరమైన గైడ్

**వాతావరణం & నేల:** చల్లని కాలంలో; సాండీ లోమ్ నేల మంచిది.

**విత్తనం:** నేరుగా విత్తండి, తర్వాత మూలాలను సరైనంగా తీయండి.

**ఎరువు:** మధ్యమ N; ఎక్కువ FYM వాడకండి లేకపోతే రూట్‌లు విభజిస్తాయి.

**నీరు:** రెగ్యులర్ నీరు; రూట్ అభివృద్ధికి నేలు తేమగా ఉండాలి.

**పురుగులు:** రూట్ ఫ్లైపై జాగ్రత్త.

**కోత:** 70–100 రోజుల్లో.
"""
    },

    "chickpea": {
        "en": """### Chickpea — Detailed Guide

**Climate & Soil:** Rabi/short-season; prefers well-drained soils.

**Sowing:** Early spring/late winter depending on region; spacing 30–45 cm.

**Fertilizer:** Moderate P and K; inoculate with rhizobium.

**Irrigation:** Minimal; avoid waterlogging.

**Pests & Diseases:** Pod borer; scouting and prompt action needed.

**Harvest:** 100–120 days when pods dry.
""",
        "hi": """### चना — विस्तृत मार्गदर्शिका

**जलवायु व मिट्टी:** रबी/संक्षिप्त मौसम की फसल; अच्छी निकास वाली मिट्टी।

**बुवाई:** क्षेत्रानुसार देर सर्दी/प्रारंभिक बसंत; दूरी 30–45 सेमी।

**उर्वरक:** मध्यम P,K; राइजोबियम इन्ोकुलेशन करें।

**सिंचाई:** कम; जलभर से बचें।

**कीट व रोग:** पाउडर बोरर/पॉड बोरर पर नजर रखें।

**कटाई:** 100–120 दिनों में जब फली सूख जाए।
""",
        "te": """### సెనగలు (Chickpea) — వివరమైన గైడ్

**వాతావరణం & నేల:** రబీ/కొద్దుదీర్ఘ కాలము; మంచి డ్రెయిన్ నేల.

**విత్తనం:** ప్రాంతం ప్రకారం శీతాకాలపు చివర లేదా వేళ్ళసమయం; స్పేసింగ్ 30–45 సెం.మీ.

**ఎరువు:** మధ్య P,K; రైజోబియం ఇనోక్యులేట్ చేయండి.

**నీరు:** తక్కువ నీరు; నీరు నిలవకుండా చూడండి.

**పురుగులు:** పొడ బోరర్ వంటి పీడలు వస్తే వెంటనే చర్య తీసుకోండి.

**కోత:** 100–120 రోజుల్లో, పొదలు పొడి అయినప్పుడు.
"""
    },

    "spinach": {
        "en": """### Spinach — Detailed Guide

**Climate & Soil:** Cool season leafy vegetable; fertile, well-drained soil.

**Sowing:** Direct sow; multiple harvests via cut-and-come again.

**Fertilizer:** Good organic matter; light N dose.

**Irrigation:** Regular shallow irrigation to keep soil moist.

**Pests & Diseases:** Leaf miners and downy mildew — monitor.

**Harvest:** 35–50 days for baby leaves; regular harvesting increases yield.
""",
        "hi": """### पालक — विस्तृत मार्गदर्शिका

**जलवायु व मिट्टी:** ठंडी ऋतु में पत्तेदार सब्जी; उर्वरक व अच्छी निकास वाली मिट्टी।

**बुवाई:** सीधे बोएं; लगातार कटाई के लिए चरणबद्ध कटाई करें।

**उर्वरक:** अच्छा जैविक पदार्थ; हल्का N दें।

**सिंचाई:** सतही नियमित सिंचाई; मिट्टी नम रखें।

**कीट व रोग:** लीफ माइनर्स, डाउनि मिल्ड्यू की निगरानी करें।

**कटाई:** 35–50 दिनों में। नियमित कटाई से उत्पादन बढ़ता है।
""",
        "te": """### పాలకూర — వివరమైన గైడ్

**వాతావరణం & నేల:** చల్లని కాలంలో పచ్చి ఆకుల పంట; బాగున్న నేల మరియు మంచి డ్రెయిన్.

**విత్తనం:** నేరుగా విత్తండి; తరచూ కోసుకుంటూ దిగుబడి పెంపొందించండి.

**ఎరువు:** మంచి ఆర్గానిక్ మ్యాటర్; తక్కువ N అవసరం.

**water:** ఉపరితలంగా తరచుగా నీరు ఇవ్వాలి.

**పురుగులు:** లీఫ్ మైనర్స్, డౌనీ మిల్డ్యూ‌పై గతిచూడండి.

**కోత:** 35–50 రోజుల్లో.
"""
    }
}

# --- Seasons and mapping to crops + short card info (days & yield) ---
seasons = {
    "summer": [
        {"key":"tomato", "days":"90-120", "yield":"40-50 tons/hectare"},
        {"key":"cucumber", "days":"60-70", "yield":"15-20 tons/hectare"},
        {"key":"okra", "days":"60-90", "yield":"10-12 tons/hectare"}
    ],
    "monsoon": [
        {"key":"rice", "days":"120-150", "yield":"4-6 tons/hectare"},
        {"key":"maize", "days":"90-110", "yield":"8-10 tons/hectare"},
        {"key":"cotton", "days":"150-200", "yield":"15-20 quintals/hectare"}
    ],
    "winter": [
        {"key":"wheat", "days":"120-150", "yield":"3-4 tons/hectare"},
        {"key":"mustard", "days":"90-120", "yield":"1-1.5 tons/hectare"},
        {"key":"pea", "days":"60-90", "yield":"2-3 tons/hectare"}
    ],
    "spring": [
        {"key":"carrot", "days":"70-100", "yield":"20-25 tons/hectare"},
        {"key":"chickpea", "days":"100-120", "yield":"1-1.5 tons/hectare"},
        {"key":"spinach", "days":"35-50", "yield":"8-10 tons/hectare"}
    ]
}

# --- Language selector ---
lang_choice = st.sidebar.radio("🌐 Language", ["English","हिन्दी","తెలుగు"])
lang_code = "en" if lang_choice=="English" else "hi" if lang_choice=="हिन्दी" else "te"
ui = translations[lang_code]

# --- Page header ---
st.markdown(f"<h2 style='color:#2E7D32'>{ui['seasonal_crops']}</h2>", unsafe_allow_html=True)
st.write(ui['subtitle'])

# --- Initialize session state for expanders (so button opens expander) ---
for crop_key in detailed_guides.keys():
    sess_key = f"open_{crop_key}"
    if sess_key not in st.session_state:
        st.session_state[sess_key] = False

# --- Season tabs ---
tab_labels = [ui['summer'], ui['monsoon'], ui['winter'], ui['spring']]
tabs = st.tabs(tab_labels)

# Helper to render a crop card with button + expander content (language aware)
def render_crop_card(crop_obj):
    key = crop_obj["key"]
    days = crop_obj["days"]
    yld = crop_obj["yield"]
    sess_key = f"open_{key}"

    # Top of card
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown(f"<div class='crop-title'>{key.capitalize()}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='badge'>{days} {ui['days_badge']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='small'><b>{ui['expected_yield']}</b> {yld}</div>", unsafe_allow_html=True)
    # Short snippet (first line of detailed guide) for quick view
    snippet = detailed_guides[key][lang_code].splitlines()
    snippet_text = " ".join([line.strip() for line in snippet[:2] if line.strip()])
    st.markdown(f"<div class='small' style='margin-top:8px'>{snippet_text}...</div>", unsafe_allow_html=True)

    # View Detailed Guide button sets session state to True for that crop
    btn = st.button(ui['view_detailed'], key=f"btn_{key}")
    if btn:
        st.session_state[sess_key] = True

    # Show expander; expanded based on session state
    expanded = st.session_state[sess_key]
    with st.expander(ui['view_detailed'], expanded=expanded):
        st.markdown(detailed_guides[key][lang_code], unsafe_allow_html=True)
        # Provide a "Close" small button to collapse (clears the flag)
        if st.button("Close", key=f"close_{key}"):
            st.session_state[sess_key] = False

    st.markdown("</div>", unsafe_allow_html=True)

# --- Render crops in each tab (3 columns) ---
for idx, season_key in enumerate(["summer","monsoon","winter","spring"]):
    with tabs[idx]:
        # season header & description (language-specific)
        season_title = ui['summer'] if season_key=="summer" else ui['monsoon'] if season_key=="monsoon" else ui['winter'] if season_key=="winter" else ui['spring']
        season_desc = {
            "en": {
                "summer":"Hot and dry conditions. Focus on heat-resistant crops with efficient water management.",
                "monsoon":"Heavy rainfall period. Ideal for water-loving crops like rice and cotton.",
                "winter":"Cool season. Favorable for vegetables and oilseed crops.",
                "spring":"Moderate weather. Ideal for fast-growing vegetables and pulses."
            },
            "hi": {
                "summer":"गरम और शुष्क मौसम। कुशल जल प्रबंधन के साथ गर्मी-प्रतिरोधी फसलों पर ध्यान दें।",
                "monsoon":"भारी वर्षा का समय। धान और कपास जैसी पानी पसंद करने वाली फसलों के लिए आदर्श।",
                "winter":"ठंड का मौसम। सब्जियों और तिलहन फसलों के लिए अनुकूल।",
                "spring":"संतुलित मौसम। जल्दी बढ़ने वाली सब्जियों और दालों के लिए उपयुक्त।"
            },
            "te": {
                "summer":"ఎండగా మరియు పొడి వాతావరణం. నీటి సమర్థ వినియోగంతో వేడి తట్టుకొనే పంటలకు దృష్టి పెట్టండి.",
                "monsoon":"భారీ వర్షకాలం. వరి మరియు పత్తి వంటి నీటిని ఇష్టపడే పంటలకు అనుకూలం.",
                "winter":"చల్లని కాలం. కూరగాయలు మరియు నూనె గింజల పంటలకు మంచిది.",
                "spring":"మధ్యస్థ వాతావరణం. త్వరగా పెరిగే కూరగాయలు మరియు పప్పులకు మంచిది."
            }
        }[lang_code][season_key]

        st.subheader(season_title + " — " + season_desc)
        crop_list = seasons[season_key]
        cols = st.columns(3)
        for i, crop in enumerate(crop_list):
            with cols[i % 3]:
                render_crop_card(crop)

# --- Footer / small note ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='font-size:13px;color:#666;'>Tip: Use the language selector on the left to switch entire page language (titles, guides, tips, buttons).</div>", unsafe_allow_html=True)
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