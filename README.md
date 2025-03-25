# E-commerce User Analytics & Purchase Prediction

This project analyzes customer behavior using the [Online Retail dataset](https://archive.ics.uci.edu/dataset/352/online+retail) from the UCI Machine Learning Repository. The dataset covers transactions from 01/12/2010 to 09/12/2011 for a UK-based online retailer.

## Project Components

1. **Data Preprocessing:**  
   - Cleans and processes the raw data.
   - File: `scripts/preprocessing.py`

2. **Exploratory Data Analysis (EDA):**  
   - Analyzes sales trends, top products, and customer behavior.
   - Notebook: `notebooks/EDA.ipynb`

3. **Predictive Modeling:**  
   - Builds a Random Forest model to predict customer purchase behavior.
   - File: `scripts/model_training.py`

4. **Dashboard Visualization:**  
   - Interactive dashboard built with Streamlit to display analytics.
   - File: `scripts/dashboard.py`

5. **API for Recommendations:**  
   - Simple API using FastAPI that provides product recommendations.
   - File: `scripts/api.py`

## How to Run

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ecommerce-analytics.git
   cd ecommerce-analytics

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   
3. **Data Preprocessing & Model Training:**
   ```bash
   python scripts/model_training.py

4. **Run the Dashboard:**
   ```bash
   streamlit run scripts/dashboard.py

5. **Run the API:**
   ```bash
   uvicorn scripts.api:app --reload

Dataset Details
Name: Online Retail

Source: [Online Retail dataset](https://archive.ics.uci.edu/dataset/352/online+retail)

Description: The dataset contains transaction data for a UK-based online retailer, including details such as InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, and Country.

Screenshots
Include screenshots or GIFs of your dashboard and API responses here.

Future Work
Extend feature engineering for improved predictive performance.

Incorporate more advanced recommendation algorithms.

Deploy the API and dashboard on cloud platforms for real-time analytics.
