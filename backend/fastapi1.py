from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

with open('Backend/model.pkl','rb') as f:
    model =pickle.load(f)

@app.get("/")
def welcome_message():
    return {"Message": "welcome to ML Project"}

@app.post("/pred")
def pred(age:int, workclass:str,education:str, educational_num:int,marital_status:str,occupation:str,relationship:str,race:str,gender:str,capital_gain:int, capital_loss:int, hours_per_weak:int, native_country: str):
    data =pd.DataFrame({
            'age':[age],
            'workclass': [workclass],
            'education': [education],
            'educational-num': [educational_num],
            'marital-status': [marital_status],
            'occupation': [occupation],
            'relationship': [relationship],
            'race': [race],
            'gender': [gender],
            'capital-gain':[capital_gain],
            'capital-loss': [capital_loss],
            'hours-per-week': [hours_per_weak],
            'native-country': [native_country]
    })

    prediction = model.predict(data)

    if prediction[0] == 1:
            result = 1

    else:
            result = 0

    return {"prediction": result}




