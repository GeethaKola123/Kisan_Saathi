import streamlit as st
import base64
from io import BytesIO
import json
import os
from PIL import Image

# ------------------ FILE PATHS ------------------
PRODUCTS_FILE = "products.json"
ORDERS_FILE = "orders.json"

# ------------------ DATA FUNCTIONS ------------------
def load_data(file):
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)
    return []

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="🌱 Agro Mitra - Marketplace", layout="wide")

# ------------------ IMAGE CONVERSION ------------------
def get_image_base64(image_file):
    if image_file is not None:
        buffered = BytesIO()
        img = Image.open(image_file)
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()
    return None

# ------------------ LOAD PRODUCTS ------------------
products_list = load_data(PRODUCTS_FILE)

# ------------------ HEADER ------------------
st.markdown("## 🌱 Agro Mitra Marketplace")
col1, col2 = st.columns([1, 2])

# ------------------ SELL SECTION ------------------
with col1:
    st.subheader("Sell Your Product")
    with st.form("sell_form"):
        f_name = st.text_input("Farmer Name")
        f_contact = st.text_input("Phone")
        p_name = st.text_input("Product Name")
        p_price = st.number_input("Price/kg", min_value=1)
        p_qty = st.number_input("Quantity (kg)", min_value=1)
        p_photo = st.file_uploader("Upload Image")
        agree = st.checkbox("I Agree")

        submit = st.form_submit_button("List Product")

        if submit:
            if not f_name or not f_contact or not p_name or not p_photo or not agree:
                st.error("Fill all details")
            else:
                img = get_image_base64(p_photo)
                new_product = {
                    "name": p_name,
                    "seller": f_name,
                    "phone": f_contact,
                    "price": p_price,
                    "qty": p_qty,
                    "img": img
                }
                products_list.append(new_product)
                save_data(PRODUCTS_FILE, products_list)
                st.success("Product Added Successfully")

# ------------------ BUY SECTION ------------------
with col2:
    st.subheader("Available Products")

    # Remove out-of-stock products dynamically
    products_list = [p for p in products_list if p["qty"] > 0]
    save_data(PRODUCTS_FILE, products_list)

    if not products_list:
        st.info("No products yet")

    for idx, product in enumerate(products_list):
        st.markdown(f"### {product['name']}")
        st.write(f"👤 {product['seller']}")
        st.write(f"💰 ₹{product['price']}/kg")
        st.write(f"📦 Stock: {product['qty']} kg")
        if product["img"]:
            st.image(base64.b64decode(product["img"]))

        c1, c2 = st.columns(2)
        with c1:
            if st.button("Contact", key=f"c{idx}"):
                st.info(f"📞 {product['phone']}")
        with c2:
            if st.button("Buy", key=f"b{idx}"):
                st.session_state[f"buy_{idx}"] = True

        # ------------------ ORDER FORM ------------------
        if st.session_state.get(f"buy_{idx}", False):
            b_qty = st.number_input(
                "Enter quantity (kg)",
                min_value=1,
                max_value=product["qty"],
                key=f"qty_live_{idx}"
            )
            total_price = b_qty * product["price"]
            st.markdown(f"### 💰 Total Price: ₹{total_price}")

            with st.form(f"order_form_{idx}"):
                b_name = st.text_input("Your Name")
                b_addr = st.text_area("Address")
                payment = st.radio("Payment", ["COD"], key=f"pay_{idx}")
                confirm = st.form_submit_button("Confirm Order")

                if confirm:
                    # Save order
                    order = {
                        "product": product["name"],
                        "buyer": b_name,
                        "address": b_addr,
                        "quantity": b_qty,
                        "total_price": total_price,
                        "payment": payment
                    }
                    orders = load_data(ORDERS_FILE)
                    orders.append(order)
                    save_data(ORDERS_FILE, orders)

                    # Reduce stock
                    products_list[idx]["qty"] -= b_qty
                    # Automatic removal if stock reaches 0
                    products_list = [p for p in products_list if p["qty"] > 0]
                    save_data(PRODUCTS_FILE, products_list)

                    st.success("Order Placed ✅")
                    st.session_state[f"buy_{idx}"] = False

# ------------------ FARMER DASHBOARD ------------------
# ------------------ FARMER DASHBOARD ------------------
st.markdown("---")
st.subheader("👨‍🌾 Farmer Orders")

orders = load_data(ORDERS_FILE)
if orders:
    for o in orders:
        st.write(f"📦 {o.get('product', 'Unknown')} → {o.get('buyer', 'Unknown')}")
        st.write(f"📦 Quantity: {o.get('quantity', 'N/A')} kg")
        st.write(f"💰 Amount: ₹{o.get('total_price', 'N/A')}")
        st.write(f"📍 {o.get('address', '')} | 💳 {o.get('payment', '')}")
        st.markdown("---")
else:
    st.write("No orders yet")