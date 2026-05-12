import streamlit as st
import time
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="CCI Smart Cooler AI", page_icon="🥤", layout="wide")

# 2. Coca-Cola Custom Branding
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF !important; }
    h1, h2, h3 { color: #F40009 !important; font-family: 'Arial Black', sans-serif !important; }
    p, label { color: #1A1A1A !important; }
    div[data-testid="stMetricValue"] > div { color: #F40009 !important; }
    div[data-testid="stMetricLabel"] > div > div > p { color: #333333 !important; font-weight: bold !important; }
    .stButton>button { background-color: #F40009 !important; color: #FFFFFF !important; font-weight: bold !important; border-radius: 8px !important; border: none !important; width: 100%; }
    .stButton>button:hover { background-color: #aa0000 !important; color: #FFFFFF !important; }
    [data-testid="stSidebar"] { background-color: #F8F9FA !important; }
    </style>
""", unsafe_allow_html=True)

# 3. Header Section
st.title("🥤 CCI Retail Execution: Smart Cooler Vision AI")
st.markdown("**BETA PoC:** Simulated Computer Vision for 'Share of Cooler' (SOC) & Asset Purity")
st.markdown("### 👨‍💻 Architected & Developed by Lokesh Kumar")
st.markdown("---")

# 4. Sidebar: Field Representative Data
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Coca-Cola_logo.svg/1200px-Coca-Cola_logo.svg.png", width=200)
st.sidebar.header("📍 Field Rep Data")
rep_name = st.sidebar.text_input("Sales Rep Name", "Lokesh Kumar")
region = st.sidebar.selectbox("Region", ["Karachi (South)", "Hyderabad / Tandojam", "Sukkur", "Lahore"])
outlet = st.sidebar.text_input("Outlet Name", "Bismillah General Store")

# 5. Main Application Logic
st.write(f"**Current Outlet:** {outlet} | **Region:** {region}")
uploaded_file = st.file_uploader("📸 Upload Cooler Image from Field", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    col_img, col_data = st.columns([1, 1.2])
    
    with col_img:
        st.image(uploaded_file, caption=f"Live Feed: {outlet}", use_container_width=True)
        
    with col_data:
        st.write("### 🧠 AI Analysis Engine")
        if st.button("🔍 Run Full Image Segmentation Scan"):
            with st.spinner("Scanning image... identifying SKUs... mapping bounding boxes..."):
                time.sleep(2)
                
            st.success("✅ Neural Network Scan Complete!")
            
            # Advanced Mock Data for Demo Purposes
            coke_portfolio = 88
            pepsi_portfolio = 4
            empty_slots = 8
            soc = (coke_portfolio / (coke_portfolio + pepsi_portfolio)) * 100
            
            # Top Level Metric Progress Bar
            st.markdown(f"#### 📊 Overall Share of Cooler (SOC): {soc:.1f}%")
            st.progress(int(soc)/100)
            st.write("---")
            
            # Detailed Metrics
            m1, m2, m3 = st.columns(3)
            m1.metric("🔴 CCI Portfolio", f"{coke_portfolio} units")
            m2.metric("🔵 Competitor", f"{pepsi_portfolio} units")
            m3.metric("⚪ Empty Slots", f"{empty_slots} slots")
            
            # Actionable Insights
            st.write("---")
            if soc >= 80:
                st.info("🟢 **STATUS PASS:** Cooler meets the 80% minimum Coca-Cola SOC standard. Asset is compliant.")
            else:
                st.error("🔴 **STATUS FAIL:** Cooler is below 80% SOC. Competitor infiltration detected.")
                
            # Advanced Charting
            st.write("**Detailed SKU Breakdown Analysis**")
            chart_data = pd.DataFrame({
                "Brand Category": ["Coca-Cola Classic", "Sprite", "Fanta", "Competitor Brands", "Empty"],
                "Detected Units": [45, 25, 18, pepsi_portfolio, empty_slots]
            })
            st.bar_chart(chart_data.set_index("Brand Category"), color="#F40009")
