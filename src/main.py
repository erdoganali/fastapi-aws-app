from fastapi import FastAPI, Depends, Request
from models import CreateUpdateChurn 
from sqlalchemy.orm import Session  
from config import model



app = FastAPI()
 

## Endpoints ######

@app.get("/")
def root_endpoint():
    return {"message": "Hello Churn Prediction API!"}

 
@app.post("/prediction/churn")
async def predict_churn(request: CreateUpdateChurn  ):
    prediction = make_churn_prediction(model, request.dict())  
    print (prediction)
    result = prediction
    return {"result:" : result}  



## functions #####

def make_churn_prediction(model, request):
    #parse input from the request
    creditScore = request["creditScore"]
    geography = request['geography']
    gender = request['gender']
    age = request['age']
    tenure = request['tenure']
    balance = request['balance']
    numOfProducts = request['numOfProducts']
    hasCrCard = request['hasCrCard']
    isActiveMember = request['isActiveMember']
    estimatedSalary = request['estimatedSalary']
    
    # Make an input vector
    person = [[creditScore, geography, gender, age, tenure, balance, numOfProducts, hasCrCard, isActiveMember, estimatedSalary]]
    
    # Predict
    prediction = model.predict(person)
  

    return prediction[0]
  