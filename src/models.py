from pydantic import BaseModel  
 
class CreateUpdateChurn(BaseModel):
    creditScore: int
    geography: str
    gender: str
    age: int
    tenure: int
    balance: float
    numOfProducts: int
    hasCrCard: int
    isActiveMember: int
    estimatedSalary: float

    # shema example : [619 'France' 'Female' 42 2 0.0 1 1 1 101348.88]
    class Config:
        schema_extra = {
            "example" : {
                "creditScore": 619, 
                "geography" : "France",
                "gender" : "Female",
                "age" : 42,
                "tenure" : 2,
                "balance" : 0.0,
                "numOfProducts" : 1,
                "hasCrCard" : 1,
                "isActiveMember" : 1,
                "estimatedSalary" : 101348.88
            }
        }