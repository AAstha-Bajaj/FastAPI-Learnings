from fastapi import FastAPI

app=FastAPI()

customer_risk_profiles ={
    101:{"name":" John Doe", "risk":"low", "score":0.12 },
    102:{"name":"Alice Smith", "risk":"medium","score":0.45},
    103:{"name":"Bob Johnson","risk":"high","score":0.89}
}

@app.get("/customers")
def get_customers(city:str, risk:str):
    return {"city":city, "risk":risk}


@app.get("/customer/{cust_id}")
def get_customer_risk(cust_id: int):
    if cust_id not in customer_risk_profiles:
        return {"error": f"customer {cust_id} not found"}

    profile = customer_risk_profiles[cust_id]
    return{
            "customer_id": cust_id,
            "name": profile["name"],
            "risk": profile["risk"],
            "score": profile["score"]
        }
        
@app.get("/model/{model_name}/customer/{cust_id}")
def get_model_customer(model_name:str,cust_id:int):
    return {"model_name":model_name, "customer_id":cust_id, "prediction":"high risk"}