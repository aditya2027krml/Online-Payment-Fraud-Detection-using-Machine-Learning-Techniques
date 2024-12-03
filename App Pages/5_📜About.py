import streamlit as st

def main():
    st.markdown("<h1 style='color: #2ecc71'>About This Project 📊💻</h1>", unsafe_allow_html=True)

    # Custom CSS styles
    st.markdown("""
    <style>
   .main { 
        font-family: Arial, sans-serif; 
    }
   .header { 
        color: #3498db; 
        font-size: 24px;
    }
   .subheader { 
        color: #666666; 
        font-size: 18px;
    }
   .steps {
        background-color: #ffe6cc; 
        padding: 10px;
        border-radius: 5px;
        margin-top: 10px;
        border: 1px solid #ccc;
        color: #000000; /* Added to make the text black */
    }
   .tech-stack {
        background-color: #c6f4d6; 
        padding: 10px;
        border-radius: 5px;
        margin-top: 10px;
        color: #000000; /* Added to make the text black */
    }
   .footer {
        color: #666666;
        margin-top: 50px;
        text-align: center;
    }
   .accent-blue {
        color: #3498db;
    }
   .accent-green {
        color: #2ecc71;
    }
   .accent-purple {
        color: #9b59b6;
    }
   .subheader-yellow {
        color: #ffff00; /* Added to make the text yellow */
    }
   .subheader-white {
        color: #ffffff; /* Added to make the text white */
    }
    </style>
    """, unsafe_allow_html=True)

    # Project Overview
    st.markdown("<h2 class='header'>Overview</h2>", unsafe_allow_html=True)
    st.write("""
        Welcome to the Online Payment Fraud Detection project. This project aims to detect fraudulent online payment transactions using machine learning techniques.
        Our application is divided into two sections: the Simple App and the Advanced App, each designed to cater to different user needs.
    """)

    # Simple App
    st.markdown("<h2 class='header'>🔎Simple User Page</h2>", unsafe_allow_html=True)
    st.write("""
        The Simple App allows users to input transaction details and quickly get a prediction on whether the transaction is fraudulent or not. 
        This app is designed for users who need a straightforward, easy-to-use interface for quick fraud detection.
    """)

    st.markdown("<h3 class='subheader subheader-yellow'>----->Steps for Prediction in Simple App</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='steps'>
        1. Enter the transaction details in the provided input fields.<br>
        2. Click the 'Predict' button.<br>
        3. View the prediction result indicating whether the transaction is fraudulent or not.
    </div>
    """, unsafe_allow_html=True)

    # Batch Predict App
    st.markdown("<h2 class='header'>🈸Batch Predict Page</h2>", unsafe_allow_html=True)
    st.write("""
        This app provides a simple and intuitive way to perform batch predictions for potential fraudulent transactions. By uploading a CSV file containing transaction data, you can quickly determine which transactions are likely to be fraudulent based on the trained XGBoost model.
    """)

    st.markdown("<h3 class='subheader subheader-yellow'>----->Steps for Prediction in Advanced App</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='steps'>
        1. Prepare your CSV data.<br>
        2. Upload the CSV file.<br>
        3. Click the "Batch Predict" button.<br>
        4. View prediction results.<br>
        5. Analyze the results (table and pie chart).
    </div>
    """, unsafe_allow_html=True)


    # Transaction History App
    st.markdown("<h2 class='header'>📂Transaction History Page</h2>", unsafe_allow_html=True)
    st.write("""
        This app allows you to view and manage your transaction history. You can easily filter transactions by type, prediction (legitimate or fraudulent), and download the data as a CSV file.
    """)

    st.markdown("<h3 class='subheader subheader-yellow'>----->Features of Transaction History Page</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='steps'>
        1. Open the app.<br>
        2. View transaction history<br>
        3. Filter transactions (optional)<br>
        4. View filtered transactions<br>
        5. Download transaction history (optional)
    </div>
    """, unsafe_allow_html=True)

    # Technology Stack
    st.markdown("<h2 class='header'>Technology Stack</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='tech-stack'>
        - Frontend: Streamlit (Python)<br>
        - Backend: Python<br>
        - Machine Learning: XGBoost, Random Forest<br>
        - Data Preprocessing: Pandas, Scikit-learn (StandardScaler)t<br>
        - Data Visualization: Matplotlibt<br>
        - Model Storage: Joblib<br>
        - CSV Handling: Pandas, Base64
    </div>
    """, unsafe_allow_html=True)


    # Footer
    st.markdown("<p class='footer'><span class='subheader-white'>Thank you for exploring our</span> <span class='accent-blue'>Online Payment Fraud Detection Project</span> . <span class='subheader-white'>We hope you find it useful and insightful.</span></p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()