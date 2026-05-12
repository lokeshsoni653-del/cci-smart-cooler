import streamlit as st
import time
import random
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="CCI Smart Cooler AI", page_icon="🥤", layout="wide")

# 2. Coca-Cola Custom Branding (Red & White)
# 2. Coca-Cola Custom Branding (Red & White)
st.markdown("""
    <style>
    /* Force main app background to clean white */
    .stApp { 
        background-color: #FFFFFF !important; 
    }
    
    /* Make headers Coca-Cola Red */
    h1, h2, h3 { 
        color: #F40009 !important; 
        font-family: 'Arial Black', sans-serif !important; 
    }
    
    /* Ensure regular text is dark grey/black for readability */
    p, label { 
        color: #1A1A1A !important; 
    }

    /* Style the metric numbers to be Red */
    div[data-testid="stMetricValue"] > div {
        color: #F40009 !important; 
    }
    
    /* Style metric labels to be bold and dark */
    div[data-testid="stMetricLabel"] > div > div > p {
        color: #333333 !important;
        font-weight: bold !important;
    }

    /* Primary button styling */
    .stButton>button { 
        background-color: #F40009 !important; 
        color: #FFFFFF !important; 
        font-weight: bold !important; 
        border-radius: 8px !important; 
        border: none !important;
    }
    .stButton>button:hover { 
        background-color: #aa0000 !important; 
        color: #FFFFFF !important; 
    }

    /* Sidebar styling to a light, professional grey */
    [data-testid="stSidebar"] {
        background-color: #F8F9FA !important;
    }
    
    /* Info/Warning box text colors */
    .stAlert p {
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Section
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
    # Display the uploaded image
    col_img, col_data = st.columns([1, 1])
    
    with col_img:
        st.image(uploaded_file, caption=f"Live Feed: {outlet}", use_container_width=True)
        
    with col_data:
        st.write("### AI Analysis Engine")
        if st.button("🔍 Run Cooler Vision AI Scan"):
            with st.spinner("Initializing neural network... detecting SKUs..."):
                time.sleep(2.5) # Simulate the time it takes for AI to process the image
                
            st.success("✅ Scan Complete! Analyzing Share of Cooler (SOC)...")
            
            # Mock Data Generation (Simulating an AI response)
            coke_facings = random.randint(45, 75)
            comp_facings = random.randint(5, 25)
            empty_slots = random.randint(0, 15)
            total_inventory = coke_facings + comp_facings
            
            # Formula for Share of Cooler
            soc = (coke_facings / total_inventory) * 100
            
            # Display Key Metrics
            st.write("---")
            m1, m2 = st.columns(2)
            m1.metric("Coca-Cola SKUs", coke_facings)
            m2.metric("Competitor SKUs", comp_facings)
            
            m3, m4 = st.columns(2)
            m3.metric("Empty Slots", empty_slots)
            m4.metric("Share of Cooler (SOC)", f"{soc:.1f}%")
            
            # Actionable Insights based on CCI Standards
            st.markdown("### 📊 Retail Compliance Report")
            if soc >= 80:
                st.info("🟢 **PASS:** Cooler meets the 80% minimum Coca-Cola SOC standard. Asset is pure.")
            else:
                st.error("🔴 **FAIL:** Cooler is below 80% SOC. Competitor infiltration detected. Issue warning to retailer.")
                
            if empty_slots > 10:
                st.warning("⚠️ **RESTOCK ALERT:** High number of empty slots. Flagging for Secondary Distribution truck dispatch.")
            
            # Visual Charting
            st.write("---")
            st.write("**Cooler Allocation Breakdown**")
            chart_data = pd.DataFrame(
                {"Categories": ["Coca-Cola", "Competitors", "Empty Slots"],
                 "Facings": [coke_facings, comp_facings, empty_slots]}
            )
            st.bar_chart(chart_data.set_index("Categories"), color="#F40009")
