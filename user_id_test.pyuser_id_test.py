import streamlit as st
import uuid

if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

user_id = st.session_state.user_id
st.write(f"Your temporary user ID: {user_id}")
