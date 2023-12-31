import streamlit as st

from catboost import CatBoostClassifier
filename = "catboost.cbm"
loaded_model = CatBoostClassifier()
loaded_model.load_model(filename)

import numpy as np


def predict_cardiovascular_disease(input_data):
    input_data = np.asarray(input_data).reshape(1, -1)
    prediction = loaded_model.predict(input_data)
    return prediction[0]

st.set_page_config(
    page_title="Cardiovascular Disease Prediction App",
    page_icon="❤️",
    layout="wide"
)

st.markdown(
    """
    <style>
        body {
            background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
            background-size: cover;
        }
        
        .color-text {
            color: red; /* Change to your desired color */
        }
        
        .stTitle {
            color: #FF5733; /* Title color */
        }
        
        .stSidebar {
            background-color: #2C3E50; /* Sidebar background color */
            color: #ffffff; /* Sidebar text color */
        }
    </style>
    """,
    unsafe_allow_html=True
)



st.title("Cardiovascular Disease Prediction App")

st.sidebar.header("User Input")
age_input = st.sidebar.number_input("Age", min_value=1, max_value=100, step=1, value=45)
gender_input = st.sidebar.radio("Gender", [1, 2])
height_input = st.sidebar.number_input("Height", min_value=1, max_value=300, step=1, value=170)
weight_input = st.sidebar.number_input("Weight", min_value=1, max_value=300, step=1, value=70)
ap_hi_input = st.sidebar.number_input("Systolic Blood Pressure (ap_hi)", min_value=1, max_value=300, step=1, value=120)
ap_lo_input = st.sidebar.number_input("Diastolic Blood Pressure (ap_lo)", min_value=1, max_value=300, step=1, value=80)
cholesterol_input = st.sidebar.radio("Cholesterol Level", [1, 2, 3])
gluc_input = st.sidebar.radio("Glucose Level", [1, 2, 3])
smoke_input = st.sidebar.checkbox("Smoker")
alco_input = st.sidebar.checkbox("Alcohol Consumer")
active_input = st.sidebar.checkbox("Active Lifestyle")

if st.sidebar.button("Predict"):
        input_data = [age_input,
                      gender_input,
                      height_input,
                      weight_input,
                      ap_hi_input,
                      ap_lo_input,
                      cholesterol_input,
                      gluc_input,
                      smoke_input,
                      alco_input,
                      active_input]
        prediction = predict_cardiovascular_disease(input_data)

        st.write("### Prediction Result:")
        if prediction == 0:
            st.write("No cardiovascular disease detected.")
        else:
            st.write("Cardiovascular disease detected.")

