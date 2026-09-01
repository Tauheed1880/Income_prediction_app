import streamlit as st
import requests

st.title("ML model with streamlit")

st.write("Salary Prediction")

age = st.number_input("Enter your age")

workclass = st.text_input("Enter your workspace")

education = st.text_input("Enter your education")

education_num = st.number_input("Enter your education number")

maritalstatus = st.text_input("Enter your Marital status")

occupation = st.text_input("Enter your occupation")

relationship = st.text_input("Enter your relationship with family")

race = st.text_input("Enter race")

gender = st.text_input("Enter your gender")

capitalgain = st.number_input("Enter your capital gain")

capitalloss = st.number_input("Enter your capital loss")

hoursperweak = st.number_input("Enter your hoursperweak")

nativecountry = st.text_input("Enter your native country name")

# prediction button 
if st.button("prediction"):

    data = {
            "age":int(age),
            "workclass":workclass,
            "education":education,
            "educational_num": int(education_num),
            "marital_status":maritalstatus,
            "occupation":occupation,
            "relationship":relationship,
            "race":race,
            "gender":gender,
            "capital_gain": int(capitalgain),
            "capital_loss": int(capitalloss),
            "hours_per_weak": int(hoursperweak),
            "native_country": nativecountry
        }
    
    # API request generate
    
    resp = requests.post("http://127.0.0.1:8000/pred", params=data)
    

    result = resp.json()
    
    if result["prediction"]==1:
        st.success("your salary is more than 50K")
    else:
        st.warning("you salary is less than 50K")