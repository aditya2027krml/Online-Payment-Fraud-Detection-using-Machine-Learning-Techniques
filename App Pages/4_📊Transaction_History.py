import streamlit as st
import pandas as pd
import os
import json

# Set page config
st.set_page_config(page_title="Transaction History", layout="wide", page_icon=":bar_chart:", initial_sidebar_state="collapsed")

# Define transaction type mappings
transaction_type_info = {
    1: "CASH_OUT",
    2: "PAYMENT",
    3: "CASH_IN",
    4: "TRANSFER",
    5: "DEBIT"
}

# Load transaction history from the file
transaction_history = []
history_file = 'transaction_history.json'

# Check if the file exists
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

# Convert all data in the transaction history to serializable types
transaction_history = [
    {
        'type': tx['type'],
        'amount': float(tx['amount']),
        'oldbalanceOrg': float(tx['oldbalanceOrg']),
        'newbalanceOrig': float(tx['newbalanceOrig']),
        'prediction': tx['prediction']
    }
    for tx in transaction_history
]

# Display the transaction history title
st.title("📊📂 Transaction History")

# Create a filter option
filter_by = st.selectbox("Filter by:", ["All", "Legitimate", "Fraudulent"])

# Display the transaction history as a table
if transaction_history:
    df_history = pd.DataFrame(transaction_history)
    df_history['type'] = df_history['type'].map(lambda x: transaction_type_info.get(x, 'Unknown'))
    
    # Apply filter
    if filter_by == "Legitimate":
        df_history = df_history[df_history['prediction'] == 0]
    elif filter_by == "Fraudulent":
        df_history = df_history[df_history['prediction'] == 1]

    # Style the table
    st.table(df_history.style.set_properties(**{'background-color': 'white', 'color': 'black', 'border-color': 'black', 'border-width': '1px', 'border-style': 'solid'}))
else:
    st.write("No transaction history yet. Please make some predictions in the 'Single Prediction' app.")

# Add a download button to download the transaction history as a CSV file
if st.button("Download CSV"):
    df_history = pd.DataFrame(transaction_history)
    df_history['type'] = df_history['type'].map(lambda x: transaction_type_info.get(x, 'Unknown'))
    csv = df_history.to_csv(index=False)
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name='transaction_history.csv',
        mime='text/csv'
    )

st.write("Developed by ADITYA KUMAR : Group A1")