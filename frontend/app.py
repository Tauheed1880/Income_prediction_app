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

hoursperweek = st.number_input("Enter your hoursperweek")

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
            "hours_per_week": int(hoursperweek),
            "native_country": nativecountry
        }
    
    # API request generate
    
    resp = requests.post(
    "https://tauheed1880-fastapi-backend.hf.space/pred",
    params=data,
    timeout=30
)

st.write("Status code:", resp.status_code)
st.write("Backend response:", resp.text)

if resp.status_code == 200:

    result = resp.json()

    if result["prediction"] == 1:
        st.success("Your salary is more than 50K")
    else:
        st.warning("Your salary is less than 50K")

else:
    st.error("Backend prediction failed.")
