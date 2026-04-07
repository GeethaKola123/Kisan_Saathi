import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import streamlit as st

# -----------------------------
# 1️⃣ Load Crop Data and Fertilizer Data
# -----------------------------
crop_data = pd.read_csv(r"C:\Users\Geetha Kola\OneDrive\Desktop\kisan_sarthi\data\crop_data.csv")
fertilizer_data = pd.read_csv(r"C:\Users\Geetha Kola\OneDrive\Desktop\kisan_sarthi\data\fertilizer.csv")

fertilizer_data.columns = fertilizer_data.columns.str.strip()
fertilizer_data.rename(columns={'Temparature': 'Temperature'}, inplace=True)

# -----------------------------
# 2️⃣ Train Crop Model
# -----------------------------
X_crop = crop_data[['N','P','K','temperature','humidity','ph','rainfall']]
y_crop = crop_data['label']
crop_model = RandomForestClassifier()
crop_model.fit(X_crop, y_crop)

# -----------------------------
# 3️⃣ Train Fertilizer Model
# -----------------------------
le_soil = LabelEncoder()
fertilizer_data['Soil Type'] = le_soil.fit_transform(fertilizer_data['Soil Type'])

le_crop = LabelEncoder()
fertilizer_data['Crop Type'] = le_crop.fit_transform(fertilizer_data['Crop Type'])

X_fert = fertilizer_data[['Temperature','Humidity','Moisture','Soil Type','Crop Type','Nitrogen','Potassium','Phosphorous']]
y_fert = fertilizer_data['Fertilizer Name']
fertilizer_model = RandomForestClassifier()
fertilizer_model.fit(X_fert, y_fert)

# -----------------------------
# 4️⃣ Advisory Function
# -----------------------------
def ai_advisory(N, P, K, temperature, humidity, ph, rainfall, moisture, soil_type):
    crop_input = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    predicted_crop = crop_model.predict(crop_input)[0]

    try:
        crop_enc = le_crop.transform([predicted_crop])[0]
    except ValueError:
        crop_enc = -1

    try:
        soil_enc = le_soil.transform([soil_type])[0]
    except ValueError:
        soil_enc = -1

    input_fert = pd.DataFrame([[temperature, humidity, moisture, soil_enc, crop_enc, N, K, P]],
                              columns=['Temperature','Humidity','Moisture','Soil Type','Crop Type','Nitrogen','Potassium','Phosphorous'])
    try:
        fert = fertilizer_model.predict(input_fert)[0]
    except:
        fert = "Fertilizer recommendation not available"

    return predicted_crop, fert

# -----------------------------
# 5️⃣ Streamlit UI
# -----------------------------
st.title("🌱 AI Advisory System")
st.write("Get Crop & Fertilizer Recommendations")

# Input form
with st.form("advisory_form"):
    N = st.number_input("Nitrogen content (N)", min_value=0, max_value=200, step=1)
    P = st.number_input("Phosphorus content (P)", min_value=0, max_value=200, step=1)
    K = st.number_input("Potassium content (K)", min_value=0, max_value=200, step=1)
    temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=60.0, step=0.1)
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, step=0.1)
    ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, step=0.1)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, step=0.1)
    moisture = st.number_input("Soil moisture (%)", min_value=0.0, max_value=100.0, step=0.1)
    soil_type = st.selectbox("Soil type", fertilizer_data['Soil Type'].unique())

    submit = st.form_submit_button("Get Recommendation")

if submit:
    crop, fert = ai_advisory(N, P, K, temperature, humidity, ph, rainfall, moisture, soil_type)
    st.success(f"🌾 Recommended Crop: **{crop}**")
    st.success(f"🧪 Recommended Fertilizer: **{fert}**")
