import firebase_admin
from firebase_admin import credentials, firestore, storage

# Replace with your Service Account JSON path
SERVICE_ACCOUNT_PATH = r"C:\Users\Geetha Kola\Downloads\serviceAccountKey.json"

# Replace with your Firebase Storage bucket name
STORAGE_BUCKET = "kisan-saathi-8bcf9.appspot.com"  # Must end with .appspot.com for Firebase

# Initialize Firebase app only once
if not firebase_admin._apps:
    cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
    firebase_admin.initialize_app(cred, {
        "storageBucket": STORAGE_BUCKET
    })

# Firestore reference
db = firestore.client()

# Storage reference
STORAGE_BUCKET = "kisan-saathi-8bcf9.firebasestorage.app"  # now correctly initialized
