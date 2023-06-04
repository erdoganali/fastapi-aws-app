from fastapi import FastAPI, Depends, Request
from models import CreateUpdateChurn, Churn
from sqlalchemy.orm import Session
from database import get_db
import config 
from config import model


app = FastAPI()
 

## Endpoints ######

@app.get("/")
def root_endpoint():
    return {"message": "Hello Churn Prediction API!"}

 
@app.post("/prediction/churn")
async def predict_churn(request: CreateUpdateChurn,
                        fastapi_req: Request,  
                        db: Session = Depends(get_db)):
    prediction = make_churn_prediction(model, request.dict()) 
    #db_insert_record = insert_request_to_db(request=request.dict(),prediction=prediction,client_ip=fastapi_req.client.host,db=db)
    #return {"db_record": db_insert_record}
    return prediction 



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
 
def insert_request_to_db(request, prediction, client_ip, db):
    new_churn = Churn(
        creditScore=request["creditScore"],
        geography=request['geography'],
        gender=request['gender'],
        age = request['age'],
        tenure = request['tenure'],
        balance = request['balance'],
        numOfProducts = request['numOfProducts'],
        hasCrCard = request['hasCrCard'],
        isActiveMember = request['isActiveMember'],
        estimatedSalary = request['estimatedSalary'],
        prediction=prediction,
        client_ip=client_ip
    )

    with db as session:
        session.add(new_churn)
        session.commit()
        session.refresh(new_churn)

    return new_churn
