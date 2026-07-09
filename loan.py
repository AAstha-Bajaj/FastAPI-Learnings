from fastapi import FastAPI
from loan_pydantic import BaseModel

app = FastAPI()

class LoanApplication(BaseModel):
    age: int
    income: float
    loan_amount: float
    employeement_years: int

@app.post("/predict")
def predict_loan(application:LoanApplication):

    #pretend this as trained model
    if application.income > 50000 and application.employeement_years > 2:
        decision = "approved"
    else:
        decision = "denied"

    return {
        "application_age": application.age,
        "decision": decision
    }

@app.get("/customer/{cust_id}")
def get_customer(cust_id: int):
    return {
        "customer_id": cust_id
    }