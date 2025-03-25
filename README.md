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
