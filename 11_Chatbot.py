import streamlit as st
import ollama
from PIL import Image

st.set_page_config(page_title="Kisan Saathi Chatbot", page_icon="🧑‍🌾")
st.title("🧑‍🌾 Kisan Saathi Chatbot")

# --- MODELS ---
TEXT_MODEL = "llama3.2:latest"  # text-only
VISION_MODEL = "llava:latest"   # small multimodal (image+text)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "warned_image" not in st.session_state:
    st.session_state.warned_image = False  # track image warning

# --- DISPLAY CHAT HISTORY ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

st.markdown("---")
col1, col2 = st.columns([1, 4])

with col1:
    uploaded_file = st.file_uploader("➕", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

with col2:
    prompt = st.chat_input("Ask Kisan Saathi...")

if prompt:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        if uploaded_file:
            st.image(uploaded_file, width=200, caption="Attached Image")

    # Decide model automatically
    model_to_use = TEXT_MODEL
    img_bytes = []

    if uploaded_file:
        model_to_use = VISION_MODEL
        img_bytes = [uploaded_file.getvalue()]
        if not st.session_state.warned_image:
            st.warning("⚠️ Using small multimodal model for image support")
            st.session_state.warned_image = True  # show warning only once

    # Generate assistant response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        try:
            response = ollama.chat(
                model=model_to_use,
                messages=[{
                    "role": "user",
                    "content": prompt,
                    "images": img_bytes
                }],
                stream=True,
            )

            for chunk in response:
                content = chunk['message']['content']
                full_response += content
                response_placeholder.markdown(full_response + "▌")

            response_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            st.error(f"Error: {e}")
            st.info(f"Check model '{model_to_use}' memory requirements")