# scripts/preprocessing.py

import pandas as pd

def load_and_clean_data(filepath):
    # Load the dataset (using latin1 encoding for special characters)
    df = pd.read_csv(filepath, encoding='latin1')
    
    # Drop rows with missing CustomerID (since customer info is critical)
    df.dropna(subset=['CustomerID'], inplace=True)
    
    # Convert InvoiceDate to datetime format
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    
    # Create TotalPrice column (Quantity * UnitPrice)
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    
    return df

if __name__ == "__main__":
    data_path = "data/online_retail.csv"
    df = load_and_clean_data(data_path)
    print("Data sample:")
    print(df.head())
