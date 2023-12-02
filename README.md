# Cardio-Vascular-Disease-Prediction
The objective of this Web app is to predict the likelihood of cardiovascular disease based on lifestyle factors



# Abstract
This project is a cardiovascular disease prediction web app developed using Streamlit and CatBoost. 
The app takes user inputs such as age, gender, blood pressure, cholesterol level, and lifestyle factors to predict the likelihood of cardiovascular disease.
It involves data preprocessing, exploratory data analysis, outlier detection, and the implementation of various classification algorithms, 
including Logistic Regression, Decision Tree, Random Forest, SVM, KNN, Naive Bayes, ADA Boost, and CatBoost.

![image](https://github.com/SharmithaYazhini/Cardio-Vascular-Disease-Prediction/assets/104150250/6b4ec852-1594-4722-98de-52cbcc1ce5bf)

I have chosen the cat boost model due to its high accuracy compared to other models. Cat Boost model achieved an accuracy of 0.73

# Data Description:

The data includes the following:
1. Age: The age of the individual (in days).
2. Height: The height of the individual (in centimetres).
3. Weight: The weight of the individual (in kilograms).
4. Gender: Categorical code representing the gender.
5. Systolic Blood Pressure (ap_hi): The systolic blood pressure measurement (Examination Feature).
6. Diastolic Blood Pressure (ap_lo): The diastolic blood pressure measurement (Examination Feature).
7. Cholesterol: Cholesterol level (1: normal, 2: above normal, 3: well above normal) (Examination Feature).
8. Glucose: Glucose level (1: normal, 2: above normal, 3: well above normal) (Examination Feature).
9. Smoking: Binary feature indicating smoking status (Subjective Feature).
10. Alcohol Intake: Binary feature indicating alcohol consumption (Subjective Feature).
11. Physical Activity: Binary feature indicating physical activity (Subjective Feature).
   
The data cleaning and preprocessing steps are implemented in the Python programming language.

![image](https://github.com/SharmithaYazhini/Cardio-Vascular-Disease-Prediction/assets/104150250/1e1f0c92-f9f8-4028-a53d-81dcb7062595) 

Link to the dataset: https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset

# Algorithm Description:

The algorithm used in this project is the *CatBoostClassifier*, a gradient-boosting algorithm optimized for categorical features. 

Various classifier algorithms, including Logistic Regression, Decision Tree, Random Forest, SVM, KNN, Naive Bayes, ADA Boost, and CatBoost were also implemented. 
Finally decided on CatBoostClassifier due to its high accuracy. (Refer mvp.py for detailed work)

The model is trained to predict the presence or absence of cardiovascular disease based on input features.

# Tools Used:

Streamlit: Used for creating the interactive web app. (app.py)

CatBoost: Implemented for building the predictive model.

NumPy: Used for numerical computations in Python.


