import streamlit as st
import pandas as pd
import joblib
from PIL import Image
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import os
import json
import numpy as np

# Load the cleaned dataset
df = pd.read_csv('Main_cleaned_dataset.csv')

# Set page config
st.set_page_config(page_title="Single Transaction Prediction", layout="wide")

# Preprocess the dataset for scaling
numerical_cols = ['amount', 'oldbalanceOrg', 'newbalanceOrig']
scaler = StandardScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# Separate features (X) and target (y)
X = df[['type', 'amount', 'oldbalanceOrg', 'newbalanceOrig']]
y = df['isFraud']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load the trained random forest model
model = joblib.load('best_randomized_model.joblib')

# Define a function to make predictions
def predict_fraud(new_data):
    new_data[numerical_cols] = scaler.transform(new_data[numerical_cols])
    prediction = model.predict(new_data)
    return prediction

# Convert numpy.int64 to int
def convert_to_serializable(data):
    if isinstance(data, dict):
        return {k: convert_to_serializable(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [convert_to_serializable(i) for i in data]
    elif isinstance(data, (int, float, str, bool, type(None))):
        return data
    elif isinstance(data, pd.Series):
        return data.tolist()
    elif isinstance(data, pd.DataFrame):
        return data.to_dict(orient='records')
    elif isinstance(data, (np.int64, np.float64)):
        return data.item()
    else:
        raise TypeError(f"Unsupported data type: {type(data)}")

# Initialize session state
if 'type_input' not in st.session_state:
    st.session_state['type_input'] = df['type'].unique()[0]
if 'amount_input' not in st.session_state:
    st.session_state['amount_input'] = 0.0
if 'oldbalanceOrg_input' not in st.session_state:
    st.session_state['oldbalanceOrg_input'] = 0.0
if 'newbalanceOrig_input' not in st.session_state:
    st.session_state['newbalanceOrig_input'] = 0.0

# Streamlit app
st.title("1️⃣ Single Prediction")

# Add a picture of an online transaction
image = Image.open("2.jfif")
st.image(image, width=350)

type_input = st.selectbox("Transaction Type", df['type'].unique(), index=list(df['type'].unique()).index(st.session_state['type_input']), key='type')
amount_input = st.number_input("Transaction Amount", min_value=0.0, value=st.session_state['amount_input'], key='amount')
oldbalanceOrg_input = st.number_input("Old Balance", min_value=0.0, value=st.session_state['oldbalanceOrg_input'], key='oldbalanceOrg')
newbalanceOrig_input = st.number_input("New Balance", min_value=0.0, value=st.session_state['newbalanceOrig_input'], key='newbalanceOrig')

# Predict button
predict_button = st.button("Predict")
clear_button = st.button("Clear", key="clear_button")

if clear_button:
    st.session_state['type_input'] = df['type'].unique()[0]
    st.session_state['amount_input'] = 0.0
    st.session_state['oldbalanceOrg_input'] = 0.0
    st.session_state['newbalanceOrig_input'] = 0.0

# Validate user inputs
if amount_input <= 0 or oldbalanceOrg_input < 0 or newbalanceOrig_input < 0:
    st.error("⚠️ Please enter valid values for Amount and Balances.")
else:
    # Handle the predict button
    if predict_button:
        st.session_state['type_input'] = type_input
        st.session_state['amount_input'] = amount_input
        st.session_state['oldbalanceOrg_input'] = oldbalanceOrg_input
        st.session_state['newbalanceOrig_input'] = newbalanceOrig_input

        new_data = pd.DataFrame({
            'type': [type_input],
            'amount': [amount_input],
            'oldbalanceOrg': [oldbalanceOrg_input],
            'newbalanceOrig': [newbalanceOrig_input]
        })
        prediction = predict_fraud(new_data)
        
        # Add transaction details to history
        transaction_history = []
        history_file = 'transaction_history.json'
        if os.path.isfile(history_file):
            with open(history_file, 'r') as f:
                try:
                    transaction_history = json.load(f)
                except json.JSONDecodeError:
                    st.error("⚠️ Warning: Corrupted transaction history file. Starting a new file.")
                    # Create a new empty file
                    transaction_history = []
                    with open(history_file, 'w') as f:
                        json.dump(transaction_history, f, indent=4)
        else:
            # Create the file if it does not exist
            with open(history_file, 'w') as f:
                json.dump(transaction_history, f, indent=4)

        # Convert prediction to int and make sure all data is serializable
        new_transaction = {
            'type': type_input,
            'amount': amount_input,
            'oldbalanceOrg': oldbalanceOrg_input,
            'newbalanceOrig': newbalanceOrig_input,
            'prediction': int(prediction[0])  # Convert int64 to standard int
        }
        transaction_history.append(new_transaction)

        # Convert all data in the transaction history to serializable types
        transaction_history = convert_to_serializable(transaction_history)
        
        # Write updated history to file
        with open(history_file, 'w') as f:
            json.dump(transaction_history, f, indent=4)

        if prediction[0] == 0:
            st.success("✅ The Predicted Class is 0️⃣✨")
            st.success("✅ This Transaction Appears to be LEGITIMATE. ✨")
        else:
            st.error("⚠️ The Predicted Class is 1️⃣ 🚨")
            st.error("⚠️ This Transaction Appears to be FRAUDULENT. 🚨")

# Define transaction type mappings
transaction_type_info = {
    1: "CASH_OUT",
    2: "PAYMENT",
    3: "CASH_IN",
    4: "TRANSFER",
    5: "DEBIT"
}

# Display information about transaction types
st.markdown("### Transaction Type Information:")
st.write("1: CASH_OUT")
st.write("2: PAYMENT")
st.write("3: CASH_IN")
st.write("4: TRANSFER")
st.write("5: DEBIT")
st.write("")

st.write("Developed by ADITYA KUMAR : Group A1")
