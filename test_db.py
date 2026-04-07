import streamlit as st
import uuid
from db_helpers import add_task, get_tasks
from datetime import datetime

# Step 0: Initialize temporary user ID
if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

user_id = st.session_state.user_id
st.write(f"Your temporary user ID: {user_id}")

# Example: Add a task
task_example = {
    "task_name": "Water the field",
    "crop_name": "Wheat",
    "due_date": "2025-09-21",
    "status": "Pending",
    "expense": 100,
    "income": 0,
    "added_time": datetime.now().strftime("%Y-%m-%d %H:%M")
}

add_task(user_id, task_example)

# Fetch tasks
tasks = get_tasks(user_id)
st.write(tasks)
