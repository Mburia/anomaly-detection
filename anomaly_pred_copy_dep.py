# -*- coding: utf-8 -*-
"""
@author: Ted Muthomi
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# heart_disease_model = pickle.load(open('C:/Users/siddhardhan/Desktop/Multiple Disease Prediction System/saved models/heart_disease_model.sav','rb'))

# parkinsons_model = pickle.load(open('C:/Users/siddhardhan/Desktop/Multiple Disease Prediction System/saved models/parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Pamoja Anomaly detection System',
                          
                          ['Targeted Patient Treatment Variables',
                           'Anomaly Insights',
                           'EMR Metric Terms'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Targeted Patient Treatment Variables'):
    
    # page title
    st.title('Anomaly detection using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Art_last_date = st.text_input('Input Weight')
        
    with col2:
        Viral_load = st.text_input('CD4 Baseline')

        # st.write('Dissagregation Monitoring')
    
    with col3:
        Pregnant_last_visit = st.text_input('Treatment Supporter(0 No 1, Yes)')
    
    with col1:
        SkinThickness = st.text_input('Input Height')
    
    with col2:
        Insulin = st.text_input('In School(0 No 1, Yes)')
    
    with col3:
        BMI = st.text_input('Input Last VL')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Input Baseline VL')

    with col2:
        Age = st.text_input('Age of the Person')
    
    with col3:
        location = st.text_input('Input Sex')

    with col1:
        Art_start = st.date_input('ART Start Date')

    with col2:
        DiagnosingDate = st.date_input('Date of Diagnosis')

    # with col1:
    #     sex = st.text_input('Input Sex')

    # with col2:
    #     doctor_conclusion = st.text_input('Doctor Conclusion')

    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Anomaly Result'):
        diab_prediction = diabetes_model.predict([[Art_last_date, Viral_load, Pregnant_last_visit, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The patient data has anomaly(s)'
        else:
          diab_diagnosis = 'No Anomaly on patient data'
        
    st.success(diab_diagnosis)