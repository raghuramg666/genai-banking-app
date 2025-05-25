import streamlit as st
import requests

BACKEND_URL = "https://a1c9ee41-1a1c-4745-854b-94f815949a91-00-3ull08k6757g7.spock.replit.dev"

st.title("💼 GenAI Banking Compliance & Risk Assistant")

# 🚨 Transaction Risk Scoring
st.header("🚨 Transaction Risk Scoring")
with st.form("txn_form"):
    user_id = st.text_input("User ID", "user001")
    amount = st.number_input("Transaction Amount", value=5000.0)
    txn_type = st.selectbox("Transaction Type", ["domestic", "international"])
    location = st.text_input("Location", "UK")
    device_type = st.selectbox("Device Type", ["web", "mobile", "atm"])
    timestamp = st.text_input("Timestamp (YYYY-MM-DDTHH:MM:SS)", "2025-05-25T10:00:00")
    submitted = st.form_submit_button("Check Risk")

    if submitted:
        payload = {
            "user_id": user_id,
            "amount": amount,
            "txn_type": txn_type,
            "location": location,
            "device_type": device_type,
            "timestamp": timestamp
        }
        try:
            res = requests.post(f"{BACKEND_URL}/txn", json=payload)
            if res.status_code == 200:
                st.success(f"✔ Risk Score: {res.json()['score']} — {res.json()['reason']}")
            else:
                st.error(f"❌ Error: {res.status_code}")
        except Exception as e:
            st.error(f"Exception: {e}")

# 📄 Compliance Q&A
st.header("📄 Compliance Assistant")
question = st.text_input("Ask a compliance-related question (e.g., AML, KYC rules)")
if st.button("Get Answer"):
    try:
        res = requests.post(f"{BACKEND_URL}/compliance-qa", json={"question": question})
        if res.status_code == 200:
            st.success(res.json()["answer"])
        else:
            st.error(f"❌ Error: {res.status_code}")
    except Exception as e:
        st.error(f"Exception: {e}")

# 📤 Upload PDF
st.header("📤 Upload Compliance PDF")
uploaded_file = st.file_uploader("Upload new policy PDF", type=["pdf"])

if uploaded_file is not None:
    files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
    try:
        res = requests.post(f"{BACKEND_URL}/upload-pdf", files=files)
        if res.status_code == 200:
            st.success(res.json()["message"])
        else:
            st.error(f"❌ Upload failed: {res.status_code}")
    except Exception as e:
        st.error(f"Exception during upload: {e}")
