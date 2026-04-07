import streamlit as st
from datetime import datetime
import re

# -----------------------
# Language setup
# -----------------------
languages = {"English": "en", "తెలుగు": "te", "हिंदी": "hi"}
lang = st.sidebar.selectbox("Select Language / భాష / भाषा", list(languages.keys()))
lang_code = languages[lang]

# -----------------------
# Translations (Added validation messages)
# -----------------------
t = {
    "en": {
        "title": "🌾 Government Schemes Eligibility Check",
        "name": "Full Name",
        "contact": "Contact Number",
        "place": "Place / Village / District",
        "aadhaar": "Aadhaar Number",
        "bank": "Bank Account Number",
        "acres": "Total Land in Acres",
        "bpl": "BPL Status",
        "annual_income": "Annual Income (₹)",
        "check": "Check Eligibility",
        "eligible": "✅ You are eligible for government schemes!",
        "not_eligible_land": "❌ Not eligible: Landholding exceeds 10 acres.",
        "not_eligible_bpl": "❌ Not eligible: Only BPL farmers are eligible.",
        "not_eligible_income": "❌ Not eligible: Annual income exceeds ₹12,00,000.",
        "fill_required": "⚠️ Please fill all required fields.",
        "invalid_aadhaar": "🚫 Aadhaar must be exactly 12 digits.",
        "invalid_bank": "🚫 Bank Account must be exactly 16 digits.",
        "available_schemes": "Available Schemes",
        "submit_apply": "Submit Application",
        "success_apply": "Successfully applied for",
    },
    "te": {
        "title": "🌾 ప్రభుత్వ పథకాల అర్హత తనిఖీ",
        "name": "పూర్తి పేరు",
        "contact": "సంప్రదింపు నంబర్",
        "place": "స్థలం / గ్రామం / జిల్లా",
        "aadhaar": "ఆధార్ నంబర్",
        "bank": "బ్యాంక్ ఖాతా నంబర్",
        "acres": "మొత్తం భూక్షేత్రం (ఏకరాల్లో)",
        "bpl": "BPL స్థితి",
        "annual_income": "వార్షిక ఆదాయం (₹)",
        "check": "అర్హత తనిఖీ చేయండి",
        "eligible": "✅ మీరు ప్రభుత్వ పథకాల కోసం అర్హులు!",
        "not_eligible_land": "❌ అర్హత లేదు: భూమి 10 ఏకరాలకంటే ఎక్కువ.",
        "not_eligible_bpl": "❌ అర్హత లేదు: కేవలం BPL రైతులు మాత్రమే అర్హులు.",
        "not_eligible_income": "❌ అర్హత లేదు: వార్షిక ఆదాయం ₹12,00,000 మించుతుంది.",
        "fill_required": "⚠️ అన్ని వివరాలను భర్తీ చేయండి.",
        "invalid_aadhaar": "🚫 ఆధార్ తప్పనిసరిగా 12 అంకెలు ఉండాలి.",
        "invalid_bank": "🚫 బ్యాంక్ ఖాతా తప్పనిసరిగా 16 అంకెలు ఉండాలి.",
        "available_schemes": "లభ్యమయ్యే పథకాలు",
        "submit_apply": "అర్జీ సమర్పించండి",
        "success_apply": "పథకం కోసం విజయవంతంగా దరఖాస్తు చేసింది",
    },
    "hi": {
        "title": "🌾 सरकारी योजनाओं की पात्रता जांच",
        "name": "पूरा नाम",
        "contact": "संपर्क नंबर",
        "place": "स्थान / गाँव / जिला",
        "aadhaar": "आधार नंबर",
        "bank": "बैंक खाता नंबर",
        "acres": "कुल भूमि (एकड़ में)",
        "bpl": "BPL स्थिति",
        "annual_income": "वार्षिक आय (₹)",
        "check": "पात्रता जांचें",
        "eligible": "✅ आप सरकारी योजनाओं के लिए पात्र हैं!",
        "not_eligible_land": "❌ पात्र नहीं: भूमि 10 एकड़ से अधिक है।",
        "not_eligible_bpl": "❌ पात्र नहीं: केवल BPL किसान पात्र हैं।",
        "not_eligible_income": "❌ पात्र नहीं: वार्षिक आय ₹12,00,000 से अधिक है।",
        "fill_required": "⚠️ सभी आवश्यक विवरण भरें।",
        "invalid_aadhaar": "🚫 आधार बिल्कुल 12 अंकों का होना चाहिए।",
        "invalid_bank": "🚫 बैंक खाता बिल्कुल 16 अंकों का होना चाहिए।",
        "available_schemes": "उपलब्ध योजनाएँ",
        "submit_apply": "आवेदन जमा करें",
        "success_apply": "योजना के लिए सफलतापूर्वक आवेदन किया गया",
    }
}

trans = t[lang_code]

# -----------------------
# Validation Helper
# -----------------------
def validate_inputs(a, b):
    # Check if Aadhaar is exactly 12 digits
    if not re.fullmatch(r'\d{12}', a):
        return "aadhaar"
    # Check if Bank is exactly 16 digits
    if not re.fullmatch(r'\d{16}', b):
        return "bank"
    return True

# -----------------------
# Dummy DB function
# -----------------------
def add_task(user_id, task_data):
    # In a real app, you'd save this to a database
    st.toast(f"System: Application Processed for {user_id}", icon="💾")

# -----------------------
# Page Title
# -----------------------
st.title(trans["title"])

# -----------------------
# Eligibility Form
# -----------------------
with st.form("eligibility_form"):
    st.subheader(trans["title"])
    name = st.text_input(trans["name"])
    contact = st.text_input(trans["contact"])
    place = st.text_input(trans["place"])
    aadhaar_input = st.text_input(trans["aadhaar"], help="12 Digits")
    bank_acc_input = st.text_input(trans["bank"], help="16 Digits")
    acres = st.number_input(trans["acres"], min_value=0.0, step=0.1)
    bpl_status = st.selectbox(trans["bpl"], ["Yes", "No"])
    annual_income = st.number_input(trans["annual_income"], min_value=0.0, step=1000.0)
    submitted = st.form_submit_button(trans["check"])

# Logic for eligibility
eligible = False
if submitted:
    val = validate_inputs(aadhaar_input, bank_acc_input)
    
    if not all([name, contact, place, aadhaar_input, bank_acc_input]):
        st.error(trans["fill_required"])
    elif val == "aadhaar":
        st.error(trans["invalid_aadhaar"])
    elif val == "bank":
        st.error(trans["invalid_bank"])
    elif acres > 10:
        st.error(trans["not_eligible_land"])
    elif bpl_status != "Yes":
        st.error(trans["not_eligible_bpl"])
    elif annual_income > 1200000:
        st.error(trans["not_eligible_income"])
    else:
        st.balloons() # Visual icon on success
        st.success(trans["eligible"])
        st.session_state['user_eligible'] = True
        # Store data in session to persist across scheme applications
        st.session_state['user_data'] = {
            "name": name, "contact": contact, "place": place, 
            "aadhaar": aadhaar_input, "bank": bank_acc_input
        }

# -----------------------
# Schemes List + Apply Form
# -----------------------
if st.session_state.get('user_eligible', False):
    st.divider()
    st.subheader(trans["available_schemes"])

    schemes = [
        {"title_en": "PM Kisan Samman Nidhi", "title_te": "PM కిసాన్ సమ్మాన్ నిధి", "title_hi":"PM किसान सम्मान निधि", 
         "desc_en": "Direct income support of ₹6,000/year.", "desc_te": "ప్రత్యక్ష ఆదాయ మద్దతు ₹6,000/సంవత్సరం.", "desc_hi":"प्रत्यक्ष आय सहायता ₹6,000/साल।"},
        {"title_en": "Crop Insurance Scheme", "title_te": "పంట బీమా పథకం", "title_hi":"फसल बीमा योजना",
         "desc_en": "Insurance coverage for crop losses.", "desc_te": "పంట నష్టాలకు బీమా కవరేజ్.", "desc_hi":"फसल हानि के लिए बीमा कवर।"},
        {"title_en": "Kisan Credit Card", "title_te": "కిసాన్ క్రెడిట్ కార్డ్", "title_hi":"किसान क्रेडिट कार्ड",
         "desc_en": "Credit facility up to ₹3 lakh.", "desc_te": "₹3 లక్షల వరకు క్రెడిట్ సౌకర్యం.", "desc_hi":"₹3 लाख तक क्रेडिट सुविधा।"}
    ]

    udata = st.session_state['user_data']

    for idx, scheme in enumerate(schemes):
        scheme_title = scheme[f"title_{lang_code}"]
        scheme_desc = scheme[f"desc_{lang_code}"]

        with st.expander(f"📝 {scheme_title}", expanded=True):
            with st.form(f"apply_form_{idx}"):
                st.write(scheme_desc)
                
                # Auto-fill from eligibility form
                f_name = st.text_input(trans["name"], value=udata["name"], key=f"f_name_{idx}")
                f_aadhaar = st.text_input(trans["aadhaar"], value=udata["aadhaar"], key=f"f_aadhaar_{idx}")
                f_bank = st.text_input(trans["bank"], value=udata["bank"], key=f"f_bank_{idx}")

                submit_apply = st.form_submit_button(f"🚀 {trans['submit_apply']}")

                if submit_apply:
                    # Validate again inside the apply form
                    val_apply = validate_inputs(f_aadhaar, f_bank)
                    
                    if val_apply == True:
                        add_task(
                            user_id=f_aadhaar,
                            task_data={
                                "scheme": scheme_title,
                                "name": f_name,
                                "time": datetime.now().strftime("%Y-%m-%d %H:%M")
                            }
                        )
                        st.success(f"🎉 {trans['success_apply']} {scheme_title}!", icon="✅")
                    elif val_apply == "aadhaar":
                        st.error(trans["invalid_aadhaar"])
                    else:
                        st.error(trans["invalid_bank"])