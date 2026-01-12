import streamlit as st
import random

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def get_crop_recommendation(n, p, k, temp, humidity, ph, rainfall):
    # Simulated recommendation logic based on some basic agricultural knowledge
    # In a real app, this would be a loaded .pkl model
    crops = {
        'Rice': {'ph': (5.5, 7.0), 'rainfall': (150, 300), 'temp': (20, 35)},
        'Maize': {'ph': (5.5, 7.5), 'rainfall': (50, 100), 'temp': (18, 30)},
        'Cotton': {'ph': (5.5, 8.5), 'rainfall': (50, 150), 'temp': (25, 35)},
        'Wheat': {'ph': (6.0, 7.5), 'rainfall': (75, 150), 'temp': (10, 25)},
        'Mango': {'ph': (5.5, 7.5), 'rainfall': (75, 250), 'temp': (25, 45)},
        'Coffee': {'ph': (5.0, 6.5), 'rainfall': (150, 250), 'temp': (15, 28)}
    }
    
    # Simple matching (weighted random for demo but with some "logic")
    best_crop = "Rice" # Default
    if ph < 6.0:
        best_crop = "Coffee"
    elif rainfall < 100:
        best_crop = "Maize"
    elif temp > 30:
        best_crop = "Cotton"
        
    return best_crop

def detect_disease(image):
    # Simulated disease detection
    # In a real app, this would be a CNN model prediction
    diseases = [
        "Healthy Leaf - No disease detected.",
        "Bacterial Spot - Possible copper-based fungicide needed.",
        "Early Blight - Ensure proper spacing and airflow.",
        "Late Blight - Check for humidity levels and use resistant varieties.",
        "Leaf Mold - Reduce overhead watering."
    ]
    return random.choice(diseases)

def card(icon, title, description):
    st.markdown(f'''
    <div class="card">
        <span class="feature-icon">{icon}</span>
        <div class="feature-title">{title}</div>
        <div class="feature-desc">{description}</div>
    </div>
    ''', unsafe_allow_html=True)
