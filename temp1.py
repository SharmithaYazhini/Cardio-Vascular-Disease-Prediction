import pickle
import streamlit as st

#from catboost import CatBoostClassifier

# Load the CatBoost model using CatBoost's load_model method 
#loaded_model=pickle.load(open("C:/Users/USER/Downloads/catboost_model.cbm","rb"))
# loaded_model = CatBoostClassifier().load_model(filename)
from catboost import CatBoostClassifier

# Define the file path
model_file_path="C:/Users/USER/Downloads/catboost_model.cbm"

# Load the CatBoost model
loaded_model = CatBoostClassifier()
loaded_model.load_model(model_file_path)

st.title("Cardio Vascular Disease Prediction")
col1, col2, col3, col4 = st.columns(4)
with col1:
  age=st.text_input("Age of the patient")
with col2:
  gender=st.text_input("Gender of the patient")
with col3:
  height=st.text_input("Height of the patient")
with col4:
  weight=st.text_input("Weight of the patient")
with col1:
  systolic=st.text_input("Systolic blood pressure of the patient")
with col2:
  diastolic=st.text_input("Diastolic Blood Pressure of the patient")
with col3:
  cho=st.text_input("Cholestral of the patient")
with col4:
  glu=st.text_input("Glucose level of the patient")
with col1:
  sm=st.text_input("Smoking status of the patient")
with col2:
  alc=st.text_input("Alcohol status of the patient")
with col3:
  act=st.text_input("Activity status of the patient")
