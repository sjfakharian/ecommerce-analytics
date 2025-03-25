# scripts/model_training.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from scripts.preprocessing import load_and_clean_data
import pickle

def create_features(df):
    # For demonstration, create a binary target: 
    # Let's assume customers with TotalPrice above median are more likely to purchase again.
    df['will_purchase_next'] = (df['TotalPrice'] > df['TotalPrice'].median()).astype(int)
    
    # Use Quantity and UnitPrice as features (this is an example – extend with more features as needed)
    features = df[['Quantity', 'UnitPrice']]
    target = df['will_purchase_next']
    return features, target

def train_model():
    df = load_and_clean_data("data/online_retail.csv")
    X, y = create_features(df)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    y_pred = clf.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save the trained model for later use in the API
    with open("model.pkl", "wb") as f:
        pickle.dump(clf, f)
    print("Model saved as model.pkl")

if __name__ == "__main__":
    train_model()
