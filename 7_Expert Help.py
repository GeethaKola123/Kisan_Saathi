import streamlit as st
from datetime import datetime
import json
import os

# ---------------------------
# File storage
# ---------------------------
STORAGE_FILE = "booking_data.json"

def load_bookings():
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_bookings(data):
    with open(STORAGE_FILE, "w") as f:
        json.dump(data, f, indent=4)

bookings = load_bookings()

# ---------------------------
# Session State
# ---------------------------
if "selected_expert" not in st.session_state:
    st.session_state.selected_expert = None

if "booking_step" not in st.session_state:
    st.session_state.booking_step = None

if "message" not in st.session_state:
    st.session_state.message = ""

# ---------------------------
# Experts Data
# ---------------------------
experts = [
    {"name": "Dr. Ravi Kumar", "education": "MBBS, MD", "city": "Hyderabad", "price": 500},
    {"name": "Dr. Sita Devi", "education": "BSc Agriculture", "city": "Vijayawada", "price": 700},
    {"name": "Dr. Ajay Sharma", "education": "MSc Soil Science", "city": "Delhi", "price": 600},
]

# ---------------------------
# Title
# ---------------------------
st.title("🧑‍🌾 Expert Booking System")

# ---------------------------
# CSS (UI Enhancements)
# ---------------------------
st.markdown("""
<style>
.card {
    background: white;
    padding: 18px;
    border-radius: 12px;
    box-shadow: 0 4px 10px #eee;
    margin-bottom: 5px;
    border: 1px solid #f0f0f0;
}
.name {
    font-size: 18px;
    font-weight: bold;
    color: #333;
}
.details {
    color: #666;
    font-size: 14px;
}
/* Styling for the Book Now button specifically */
div.stButton > button {
    background-color: #2196F3 !important;
    color: white !important;
    width: 100%;
    border-radius: 8px;
    height: 3em;
    transition: 0.3s;
}
div.stButton > button:hover {
    background-color: #1976D2 !important;
    border-color: #1976D2 !important;
    transform: translateY(-2px);
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Expert Cards
# ---------------------------
for i, exp in enumerate(experts):

    st.markdown(f"""
    <div class="card">
        <div class="name">{exp['name']}</div>
        <div class="details">{exp['education']} • {exp['city']}</div>
        <div class="details">💰 <b>₹{exp['price']}</b></div>
    </div>
    """, unsafe_allow_html=True)

    # Simplified to just the Booking Button
    if st.button(f"📅 Book Appointment with {exp['name']}", key=f"book{i}"):
        st.session_state.selected_expert = exp
        st.session_state.booking_step = "form"
        st.session_state.message = ""
        st.rerun() # Refresh to show form immediately

# ---------------------------
# Booking Form
# ---------------------------
if st.session_state.booking_step == "form":
    exp = st.session_state.selected_expert
    st.markdown("---")
    st.subheader(f"📌 Booking with {exp['name']}")

    with st.form("booking_form"):
        col_a, col_b = st.columns(2)
        with col_a:
            date = st.date_input("Select Date", min_value=datetime.today())
        with col_b:
            time = st.time_input("Select Time")
        
        problem = st.text_area("Describe your issue/requirements")
        payment = st.selectbox("Payment Method", ["UPI", "Card", "Cash"])

        submit = st.form_submit_button("Proceed to Payment")

        if submit:
            st.session_state.temp_booking = {
                "name": exp['name'],
                "education": exp['education'],
                "city": exp['city'],
                "price": exp['price'],
                "date": date.strftime("%d-%m-%Y"),
                "time": time.strftime("%H:%M"),
                "problem": problem,
                "payment": payment
            }
            st.session_state.booking_step = "payment"
            st.rerun()

# ---------------------------
# Payment
# ---------------------------
if st.session_state.booking_step == "payment":
    data = st.session_state.temp_booking
    st.markdown("---")
    st.subheader("💳 Secure Payment")
    
    st.info(f"Summary: Appointment with {data['name']} for ₹{data['price']}")

    if st.button("✅ Confirm & Pay Now"):
        booking_id = f"{data['name']}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        bookings[booking_id] = data
        save_bookings(bookings)

        st.session_state.message = "🎉 Booking Confirmed Successfully!"
        st.session_state.booking_step = None
        st.rerun()

# ---------------------------
# Messages
# ---------------------------
if st.session_state.message:
    st.success(st.session_state.message)

# ---------------------------
# Show Bookings
# ---------------------------
st.markdown("---")
st.subheader("📂 Your Scheduled Bookings")

if bookings:
    for b in reversed(list(bookings.values())):
        st.markdown(f"""
        <div style="background:#f1f8ff; padding:15px; border-left: 5px solid #2196F3; border-radius:8px; margin-bottom:10px;">
        <span style="font-weight:bold; font-size:16px;">👤 {b.get('name','-')}</span><br>
        <small>{b.get('education','N/A')} • {b.get('city','N/A')}</small><br>
        <p style="margin: 8px 0;">📝 <i>{b.get('problem','-')}</i></p>
        📅 <b>{b.get('date','-')}</b> at ⏰ <b>{b.get('time','-')}</b><br>
        💰 Paid via {b.get('payment','-')} | <span style="color:green;"><b>₹{b.get('price','-')}</b></span>
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("No bookings found.")