import streamlit as st
from utils import local_css, card, get_crop_recommendation, detect_disease
from PIL import Image
import io
import random

# Page Config
st.set_page_config(
    page_title="AgriPred - AI Agriculture Assistant",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load CSS
local_css("style.css")

# Add Floating Leaves Background
def add_leaves():
    leaf_html = ""
    for _ in range(15):
        left = random.randint(0, 100)
        duration = random.randint(10, 25)
        delay = random.randint(0, 5)
        size = random.randint(15, 35)
        leaf_html += f'<div class="leaf" style="left: {left}%; animation-duration: {duration}s; animation-delay: {delay}s; width: {size}px; height: {size}px;"></div>'
    st.markdown(leaf_html, unsafe_allow_html=True)

add_leaves()

# Sidebar Navigation (Removed Home)
st.sidebar.markdown("<h2 style='text-align: center;'>🌱 AgriPred</h2>", unsafe_allow_html=True)
page = st.sidebar.radio("Navigate Tools", ["🌾 Crop Recommendation", "🍃 Disease Detection"])

st.sidebar.markdown("---")
st.sidebar.info(
    "AgriPred uses AI to help farmers make data-driven decisions. "
    "Select a tool above to get started."
)

# Shared Header
st.markdown("<h1 class='main-title'>AgriPred</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Precision Agriculture Powered by AI</p>", unsafe_allow_html=True)

if page == "🌾 Crop Recommendation":
    st.markdown("### 🌾 Crop Finder")
    st.write("Determine the most fertile crop for your land using soil nutrients and climate data.")
    
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("#### Soil Nutrients")
            n = st.number_input("Nitrogen (N)", min_value=0, max_value=140, value=50, help="Nitrogen content in soil")
            p = st.number_input("Phosphorus (P)", min_value=0, max_value=140, value=50, help="Phosphorus content in soil")
            k = st.number_input("Potassium (K)", min_value=0, max_value=140, value=50, help="Potassium content in soil")
            
        with col2:
            st.markdown("#### Climate Factors")
            temp = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0)
            humidity = st.number_input("Humidity (%)", min_value=0, max_value=100, value=50)
            
        with col3:
            st.markdown("#### Soil Properties")
            ph = st.number_input("pH Value", min_value=0.0, max_value=14.0, value=6.5)
            rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=100.0)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Generate Recommendation"):
            recommendation = get_crop_recommendation(n, p, k, temp, humidity, ph, rainfall)
            st.markdown(f'''
            <div style="background: rgba(46, 125, 52, 0.1); border-radius: 15px; padding: 20px; text-align: center; border: 1px solid var(--primary-color);">
                <h2 style="color: var(--primary-color) !important; margin: 0;">Optimal Crop Found: {recommendation}</h2>
            </div>
            ''', unsafe_allow_html=True)
            st.balloons()
            
        st.markdown('</div>', unsafe_allow_html=True)

elif page == "🍃 Disease Detection":
    st.markdown("### 🍃 Health Scanner")
    st.write("Upload a leaf image to instantly diagnose plant health and diseases.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Drop your leaf image here", type=["jpg", "png", "jpeg"])
        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, caption="Analyzable Specimen", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
            
    with col2:
        if uploaded_file:
            st.markdown('<div class="card" style="height: 100%;">', unsafe_allow_html=True)
            st.markdown("### Diagnosis Engine")
            if st.button("Start AI Scan"):
                with st.spinner("Analyzing biological patterns..."):
                    import time
                    time.sleep(2) 
                    result = detect_disease(image)
                    st.markdown(f'''
                    <div style="padding: 20px; border-radius: 12px; border: 2px dashed #4caf50; background: rgba(255,255,255,0.5);">
                        <h4 style="margin: 0; color: #1b5e20;">Scan Result:</h4>
                        <p style="font-size: 1.2rem; margin-top: 10px;">{result}</p>
                    </div>
                    ''', unsafe_allow_html=True)
                    if "Healthy" in result:
                        st.success("Analysis complete: Plant is in optimal health.")
                    else:
                        st.warning("Analysis complete: Pathogens detected. Consult treatment guide.")
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.info("Awaiting input: Please upload a leaf image to begin the scanning sequence.")

st.markdown("---")
st.caption("© 2026 AgriPred | Built with passion for sustainable farming.")
