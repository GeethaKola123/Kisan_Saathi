from firebase_config import db
from datetime import datetime

# ------------------ TASKS ------------------
def add_task(user_id, task_data):
    db.collection("users").document(user_id).collection("tasks").add(task_data)

def get_tasks(user_id):
    docs = db.collection("users").document(user_id).collection("tasks").order_by("added_time").stream()
    return [doc.to_dict() for doc in docs]

# ------------------ TRANSACTIONS ------------------
def add_transaction(user_id, txn_data):
    db.collection("users").document(user_id).collection("transactions").add(txn_data)

def get_transactions(user_id):
    docs = db.collection("users").document(user_id).collection("transactions").order_by("date").stream()
    return [doc.to_dict() for doc in docs]

# ------------------ PEST QUERIES ------------------
def add_pest_query(user_id, query_data):
    db.collection("users").document(user_id).collection("pest_queries").add(query_data)

def get_pest_queries(user_id):
    docs = db.collection("users").document(user_id).collection("pest_queries").stream()
    return [doc.to_dict() for doc in docs]

# ------------------ SUCCESS STORIES ------------------
def add_success_story(user_id, story_data):
    db.collection("users").document(user_id).collection("success_stories").add(story_data)

def get_success_stories(user_id):
    docs = db.collection("users").document(user_id).collection("success_stories").stream()
    return [doc.to_dict() for doc in docs]
