from fastapi import FastAPI

app=FastAPI()

all_customer =[
    {"id":"1","name":"john", "city":"bangalore","risk":"low"},
    {"id":"2","name":"jony", "city":"mumbai", "risk":"medium"},
    {"id":"3","name":"jonny", "city":"bangalore","risk":"high"},
    {"id":"4","name":"jack", "city":"chennai", "risk":"low"},
    {"id":"5","name":"jeck", "city":"hyderabad", "risk":"medium"},
    {"id":"6","name":"jon", "city":"hyderabad", "risk":"high"}
]

@app.get("/customers")
def get_customers(city:str, risk:str):
    filtered = [
        c for c in all_customer
        if c["city"] == city and c["risk"] == risk
    ]
    
    return {
        "city":city, 
        "risk": risk,
        "customer_count": len(filtered),
        "results": filtered
    }