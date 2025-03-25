# scripts/api.py

from fastapi import FastAPI
import uvicorn
import pandas as pd

app = FastAPI()

# Load the dataset (for simplicity, using the raw data)
df = pd.read_csv("data/online_retail.csv", encoding='latin1')

@app.get("/")
def read_root():
    return {"message": "Welcome to the E-commerce API!"}

@app.get("/recommendations/{customer_id}")
def get_recommendations(customer_id: int):
    # Dummy recommendation logic:
    customer_data = df[df['CustomerID'] == customer_id]
    if customer_data.empty:
        return {"error": "Customer not found."}
    # Recommend the product with the highest quantity purchased by this customer
    recommended_product = customer_data.groupby("Description")["Quantity"].sum().idxmax()
    return {"customer_id": customer_id, "recommended_product": recommended_product}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
