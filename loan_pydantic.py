from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class LoanApplication(BaseModel):
    name: str
    age: int
    income: float
    loan_amount: float
    employeement_years: int

@app.post("/predict")
def predict_loan(application:LoanApplication):
    approved =(
        application.income>50000 and 
        application.employeement_years > 2 and
        application.age >=21
    )

    return{
        "decision": "approved" if approved else "rejected",
        "name": application.name,
        "loan_amount": application.loan_amount,
        "reviewed_income": application.income
        } 