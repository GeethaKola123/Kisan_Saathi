import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# 1. Load dataset
data = pd.read_csv("data/fertilizer.csv")   # 👈 mee fertilizer dataset name
print("Dataset loaded successfully!")
print(data.head())

# 2. Encode categorical columns (exact column names from dataset)
encoder_crop = LabelEncoder()
encoder_soil = LabelEncoder()
encoder_fert = LabelEncoder()

data["Crop Type"] = encoder_crop.fit_transform(data["Crop Type"])
data["Soil Type"] = encoder_soil.fit_transform(data["Soil Type"])
data["Fertilizer Name"] = encoder_fert.fit_transform(data["Fertilizer Name"])

# 3. Features (X) & Target (y)
X = data.drop(columns=["Fertilizer Name"])
y = data["Fertilizer Name"]

# 4. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Train Random Forest Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. Evaluate Model
acc = model.score(X_test, y_test)
print("Accuracy:", acc)

# 7. Save Model & Encoders
joblib.dump(model, "models/fert_model.pkl")
joblib.dump(encoder_crop, "models/fert_crop_encoder.pkl")
joblib.dump(encoder_soil, "models/fert_soil_encoder.pkl")
joblib.dump(encoder_fert, "models/fert_label_encoder.pkl")

print("✅ Fertilizer model trained & saved in 'models/' folder!")
