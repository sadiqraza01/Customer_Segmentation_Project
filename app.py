import streamlit as st
import pickle
import numpy as np

# -------------------------------
# Load Pretrained GMM Model and Scaler
# -------------------------------
with open('gmm_model.pkl', 'rb') as f:
    gmm_model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# -------------------------------
# Manual Mappings
# -------------------------------
mappings_education = {'Basic': 0, 'Graduation': 1, 'Master': 2, 'PhD': 3}
mappings_marital = {'Single': 0, 'Married': 1, 'Divorced': 2, 'Together': 3, 'Widow': 4}

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🎯 Customer Segmentation (GMM Modelling)")
st.subheader("🧾 Enter Customer Details")

education_input = st.selectbox("📚 Education Level", list(mappings_education.keys()))
marital_input = st.selectbox("💍 Marital Status", list(mappings_marital.keys()))
income_input = st.slider("💰 Income", 0, 1000000, 70000, step=1000)
kidhome_input = st.number_input("👶 Number of Kids at Home", min_value=0, max_value=5, step=1)
teenhome_input = st.number_input("🧒 Number of Teens at Home", min_value=0, max_value=5, step=1)

mnt_wines_input = st.slider("🍷 Spending on Wine (₹)", 0, 2000, 300)
mnt_meat_input = st.slider("🥩 Spending on Meat (₹)", 0, 2000, 500)
mnt_fish_input = st.slider("🐟 Spending on Fish (₹)", 0, 2000, 150)
mnt_sweets_input = st.slider("🍬 Spending on Sweets (₹)", 0, 2000, 100)
mnt_gold_input = st.slider("💍 Spending on Gold Products (₹)", 0, 2000, 250)

num_deals_input = st.slider("💸 Deal Purchases", 0, 15, 3)
num_web_input = st.slider("🌐 Web Purchases", 0, 15, 5)
num_catalog_input = st.slider("📘 Catalog Purchases", 0, 15, 4)
num_store_input = st.slider("🏬 Store Purchases", 0, 15, 6)
recency_input = st.slider("📆 Recency (Days since last purchase)", 0, 100, 30)

# -------------------------------
# Map categorical inputs
# -------------------------------
education_mapped = mappings_education[education_input]
marital_mapped = mappings_marital[marital_input]

# -------------------------------
# Create feature array
# -------------------------------
features = np.array([[education_mapped, marital_mapped, income_input, kidhome_input,
                      teenhome_input, mnt_wines_input, mnt_meat_input,
                      mnt_fish_input, mnt_sweets_input, mnt_gold_input,
                      num_deals_input, num_web_input, num_catalog_input,
                      num_store_input, recency_input]])

# -------------------------------
# Scale the input features
# -------------------------------
scaled_features = scaler.transform(features)

# -------------------------------
# Predict GMM Segment
# -------------------------------
if st.button("🔍 Predict Segment"):
    segment = gmm_model.predict(scaled_features)
    st.success(f"Predicted Customer Segment: {segment[0]}")
