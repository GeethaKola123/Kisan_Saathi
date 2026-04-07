import pandas as pd

df = pd.read_csv("data/crop_data.csv")
print(df.head())
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# 1. Load dataset
df = pd.read_csv("data/crop_data.csv")
print("Dataset loaded successfully!")
print(df.head())

# 2. Features and Target
X = df.drop(columns=['label'])   # all inputs
y = df['label']                  # target

# 3. Encode target (crop names → numbers)
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Save label encoder for later use
joblib.dump(le, "models/crop_label_encoder.pkl")

# 4. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# 5. Train Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. Evaluate model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# 7. Save trained model
joblib.dump(model, "models/crop_model.pkl")
print("✅ Crop model trained & saved in 'models/' folder!")
