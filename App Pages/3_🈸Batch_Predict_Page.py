import streamlit as st
import pandas as pd
import joblib
import base64
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv('Main_cleaned_dataset.csv')

# Set page config
st.set_page_config(page_title="Batch Prediction", page_icon="🕵️‍♀️")

# Preprocess the dataset for scaling
numerical_cols = ['amount', 'oldbalanceOrg', 'newbalanceOrig']
scaler = StandardScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# Separate features (X) and target (y)
X = df[['type', 'amount', 'oldbalanceOrg', 'newbalanceOrig']]
y = df['isFraud']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load the trained Random Forest model
model = joblib.load('best_randomized_model.joblib')

# Define a function to make predictions
def predict_fraud(new_data):
    new_data[numerical_cols] = scaler.transform(new_data[numerical_cols])
    return model.predict(new_data)

# Streamlit app
st.title("🕵️‍♀️ Batch Prediction")

# Batch prediction
uploaded_file = st.file_uploader("Upload CSV for batch prediction", type=["csv"], help="Select a CSV file containing transaction data for batch prediction.")

if uploaded_file is not None:
    batch_data = pd.read_csv(uploaded_file)
    
    # Display the uploaded CSV file
    st.write("Uploaded CSV:")
    st.dataframe(batch_data)
    
    # Add a button for batch prediction
    st.markdown("<style>.button {background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;}</style>", unsafe_allow_html=True)
    predict_button = st.button("Batch Predict", type="primary")
    
    if predict_button:
        # Ensure the required columns are present
        required_columns = set(numerical_cols + ['type'])
        if not required_columns.issubset(batch_data.columns):
            st.error(f"The uploaded CSV file must contain the following columns: {', '.join(required_columns)}")
        else:
            # Preprocess the batch data before prediction (but don't modify the original dataframe)
            batch_data_preprocessed = batch_data.copy()  # Create a copy to avoid modifying the original
            batch_data_preprocessed[numerical_cols] = scaler.transform(batch_data_preprocessed[numerical_cols])
            batch_predictions = predict_fraud(batch_data_preprocessed)

            # Create a new dataframe with the predicted 'isFraud' column and the original features 
            predicted_df = batch_data.copy()
            predicted_df['isFraud'] = batch_predictions
            
            # Display batch prediction results
            st.write("Batch Predictions:")
            st.dataframe(predicted_df)
            
            # Display additional statistics
            total_samples = len(batch_data)
            fraud_samples = sum(predicted_df['isFraud'])
            non_fraud_samples = total_samples - fraud_samples
            
            st.write(f"Total Samples: {total_samples}")
            st.write(f"Fraud Samples: {fraud_samples}")
            st.write(f"Non-Fraud Samples: {non_fraud_samples}")
            
            # Create a pie chart
            fig, ax = plt.subplots(figsize=(4, 3))  # Adjust the figure size here
            ax.set_title("Fraud vs Non-Fraud Distribution")
            labels = ['Fraud', 'Non-Fraud']
            sizes = [fraud_samples, non_fraud_samples]
            colors = ['#ff0000','#008000']
            explode = (0.1, 0)  # explode 1st slice
            ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140, colors=colors)
            st.pyplot(fig)
            
            # Add a download button for the batch prediction table
            st.write("Download Batch Prediction Table:")
            csv = predicted_df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
            href = f'<a href="data:file/csv;base64,{b64}" download="batch_prediction.csv">Download CSV File</a>'
            st.markdown(href, unsafe_allow_html=True)
