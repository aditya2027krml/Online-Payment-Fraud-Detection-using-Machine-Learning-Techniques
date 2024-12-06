# *💳 Online Payment Fraud Detection Using Machine Learning 🚀*
### Welcome to the ultimate solution for secure online transactions!
🔍 Say goodbye to payment fraud with our cutting-edge machine learning-based detection system. This repository hosts not only the project but also a sleek, interactive Streamlit app for hands-on use!

## 🎯 Project Highlights
Built Using: Advanced ML techniques for accurate fraud detection.

Milestone-Driven Development:

### 🛠 Milestone 1: Data Preprocessing
Every great machine learning model starts with clean, reliable data! Here's how we prepared ours:

**🧹 Missing Values Handling:** Replaced or removed missing values for consistent datasets.

**🧮 Feature Scaling:** Standardized numerical features for improved model performance.

**🔎 Outlier Detection:** Identified and mitigated outliers to enhance accuracy.

**🎨 Feature Engineering:**
- Created meaningful features to enrich the dataset.
- Added time-based features like transaction hours for deeper insights.
  
**⚖️ Class Imbalance Handling:**
- Applied SMOTE (Synthetic Minority Oversampling Technique) to balance the dataset, ensuring fairness in fraud detection.
  
### 🔍 Milestone 2: Model Selection and Implementation
After preparing the data, we dove into the world of algorithms. Here's what we did:

**🤖 Tried and Tested Algorithms:**
- Logistic Regression
- Random Forest
- Decision Trees
- Support Vector Machines (SVM)
- XGBoost
  
**🏆 Final Model:**
After extensive experimentation, we chose **XGBoost** for its exceptional performance in accuracy and precision.
Why XGBoost? It's fast, efficient, and excels at handling imbalanced datasets like ours.

## 🎥 Streamlit Web App 🎉
We’ve created a user-friendly multi-page Streamlit app to make fraud detection accessible to everyone!

### Pages Overview 🖱️

- 🏠 Home Page: Your starting point for all features.
- 🤔 Simple User Page: Intuitive prediction interface for individual transactions.
- 📂 Batch Predict Page: Upload files for bulk fraud analysis.
- 📜 Transaction History: Review past transactions and their predictions.
- ℹ️ About App: Learn about the app and how it works.
- 🔎 More About the Page App: Dive deeper into its workings and features.

## 🏃 How to Run the App
🖥️ Follow these steps to get started:
In bash
1. Install Streamlit:

- pip install streamlit  

2. Run the Home Page:
   
- streamlit run 0_💰Home_page.py  
