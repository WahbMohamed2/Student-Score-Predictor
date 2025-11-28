import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image

# Load preprocessor and model
preprocessor = joblib.load(".\\models\\preprocessor.pkl")
model = joblib.load(".\\models\\Ridge_model.pkl")

# Streamlit page config
st.set_page_config(
    page_title="Student Exam Score Predictor",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS styling inspired by the progress report design
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');
    
    /* Global styling */
    .stApp {
        background: linear-gradient(135deg, #f5f5f0 0%, #e8e8dc 100%);
        font-family: 'Montserrat', sans-serif;
    }
    
    /* Main container */
    .main .block-container {
        padding: 2rem 3rem;
        max-width: 900px;
        background: white;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin-top: 2rem;
        margin-bottom: 2rem;
    }
    
    /* Title styling */
    h1 {
        color: #8a9a7a !important;
        font-weight: 700 !important;
        text-align: center !important;
        font-size: 2.5rem !important;
        margin-bottom: 0.5rem !important;
        letter-spacing: 2px !important;
        text-transform: uppercase;
    }
    
    /* Subtitle/description */
    .stMarkdown p {
        color: #666;
        text-align: center;
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    
    /* Section headers */
    .section-header {
        background: linear-gradient(90deg, #c17a6e 0%, #d89380 100%);
        color: white !important;
        padding: 15px 20px;
        border-radius: 8px;
        font-weight: 600;
        font-size: 1.1rem;
        margin: 2rem 0 1.5rem 0;
        text-align: center;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    
    /* Input fields styling */
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select {
        border: 2px solid #d4d9c8 !important;
        border-radius: 8px !important;
        padding: 10px !important;
        font-size: 1rem !important;
        background: #fafaf5 !important;
        transition: all 0.3s ease;
    }
    
    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #8a9a7a !important;
        box-shadow: 0 0 0 2px rgba(138, 154, 122, 0.1) !important;
    }
    
    /* Labels */
    .stNumberInput > label,
    .stSelectbox > label {
        color: #555 !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #8a9a7a 0%, #a4b89a 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 15px 50px !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        letter-spacing: 1px !important;
        text-transform: uppercase !important;
        box-shadow: 0 5px 15px rgba(138, 154, 122, 0.3) !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        margin-top: 2rem !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 20px rgba(138, 154, 122, 0.4) !important;
        background: linear-gradient(135deg, #7a8a6a 0%, #94a88a 100%) !important;
    }
    
    /* Success message */
    .stSuccess {
        background: linear-gradient(90deg, #8a9a7a 0%, #a4b89a 100%) !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 20px !important;
        font-size: 1.3rem !important;
        font-weight: 600 !important;
        text-align: center !important;
        margin-top: 2rem !important;
        box-shadow: 0 5px 15px rgba(138, 154, 122, 0.3) !important;
    }
    
    /* Grade scale table styling */
    .grade-scale {
        background: linear-gradient(135deg, #8a9a7a 0%, #a4b89a 100%);
        color: white;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        font-weight: 600;
        margin: 2rem 0 1rem 0;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    
    .grade-table {
        background: #faf9f0;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 2rem;
    }
    
    .grade-row {
        display: flex;
        justify-content: space-between;
        padding: 8px 15px;
        color: #555;
        font-size: 0.95rem;
    }
    
    /* Column layout */
    .row-widget.stHorizontal {
        gap: 1rem;
    }
    
    /* Sidebar styling */
    .css-1d391kg, [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #8a9a7a 0%, #a4b89a 100%);
    }
    
    /* Info box */
    .info-box {
        background: #faf9f0;
        border-left: 4px solid #8a9a7a;
        padding: 15px;
        border-radius: 5px;
        margin: 1rem 0;
        color: #555;
    }
</style>
""", unsafe_allow_html=True)

# Logo
try:
    from PIL import Image
    logo = Image.open("./assets/image.png")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(logo, use_container_width=True)
except:
    st.markdown("""
    <div style='text-align: center; margin-bottom: 1rem;'>
        <div style='display: inline-block; border: 2px dashed #8a9a7a; padding: 20px 40px; border-radius: 5px;'>
            <p style='margin: 0; color: #8a9a7a; font-size: 0.9rem; font-weight: 600;'>YOUR LOGO</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.title("Student Score Predictor")
st.markdown("""
Enter student information below to predict their exam score based on lifestyle factors.
""")

# Define input fields
def user_input_features():
    # Personal Information Section
    st.markdown('<div class="section-header">📋 Personal Information</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=10, max_value=100, value=18)
        gender = st.selectbox("Gender", ["Female", "Male", "Other"])
    with col2:
        parental_education_level = st.selectbox(
            "Parental Education Level", ["High School", "Bachelor", "Master"]
        )
        part_time_job = st.selectbox("Part-Time Job", ["No", "Yes"])
    
    # Academic Information Section
    st.markdown('<div class="section-header">📚 Academic Information</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        study_hours_per_day = st.number_input(
            "Study Hours per Day", min_value=0, max_value=24, value=3
        )
        attendance_percentage = st.number_input(
            "Attendance Percentage", min_value=0, max_value=100, value=90
        )
    with col2:
        internet_quality = st.selectbox("Internet Quality", ["Poor", "Average", "Good"])
        extracurricular_participation = st.selectbox(
            "Extracurricular Participation", ["No", "Yes"]
        )
    
    # Lifestyle Information Section
    st.markdown('<div class="section-header">🌟 Lifestyle & Wellness</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        sleep_hours = st.number_input(
            "Sleep Hours per Day", min_value=0, max_value=24, value=7
        )
        diet_quality = st.selectbox("Diet Quality", ["Poor", "Fair", "Good"])
        exercise_frequency = st.selectbox(
            "Exercise Frequency",
            ["Very inactive", "Occasionally active", "Frequently exercises"],
        )
    with col2:
        social_media_hours = st.number_input(
            "Social Media Hours per Day", min_value=0, max_value=24, value=2
        )
        netflix_hours = st.number_input(
            "Netflix Hours per Day", min_value=0, max_value=24, value=1
        )
        mental_health_rating = st.selectbox(
            "Mental Health Rating",
            ["Low well-being", "Moderate well-being", "High well-being"],
        )

    data = {
        "age": age,
        "study_hours_per_day": study_hours_per_day,
        "social_media_hours": social_media_hours,
        "netflix_hours": netflix_hours,
        "attendance_percentage": attendance_percentage,
        "sleep_hours": sleep_hours,
        "gender": gender,
        "part_time_job": part_time_job,
        "diet_quality": diet_quality,
        "parental_education_level": parental_education_level,
        "internet_quality": internet_quality,
        "extracurricular_participation": extracurricular_participation,
        "exercise_frequency": exercise_frequency,
        "mental_health_rating": mental_health_rating,
    }
    features = pd.DataFrame([data])
    return features


input_df = user_input_features()

# Predict button
if st.button("Predict Exam Score"):
    input_prepared = preprocessor.transform(input_df)
    prediction = model.predict(input_prepared)
    
    # Cap the score between 0 and 100
    predicted_score = max(0, min(100, prediction[0]))
    
    st.success(f"Predicted Exam Score: {predicted_score:.2f}")
    
    # Grade Scale Reference
    st.markdown('<div class="grade-scale">Grade Scale Reference</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="grade-table">
        <div class="grade-row"><span><b>A+ 97-100</b></span><span><b>C 70-76</b></span></div>
        <div class="grade-row"><span>A 90-96</span><span>D+ 67-69</span></div>
        <div class="grade-row"><span>B+ 87-89</span><span>D 60-66</span></div>
        <div class="grade-row"><span>B 80-86</span><span>F 26-59</span></div>
        <div class="grade-row"><span>C+ 77-79</span><span>F 1-25</span></div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style='text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 2px solid #e0e0d0; color: #888; font-size: 0.9rem;'>
    <p>Student Performance Prediction System</p>
</div>
""", unsafe_allow_html=True)