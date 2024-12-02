import streamlit as st
import time

# Set the page title and layout
st.set_page_config(page_title="Online Payment Fraud Detection using Machine Learning", page_icon="💰", layout="wide")

# Load Google Fonts and apply custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

body {
    font-family: 'Roboto', sans-serif;
    background-color: #f0f0f0;  /* Light gray background */
    padding: 20px;
}

.title-text {
    text-align: center;
    color: #FFFF00;
    font-style: italic;
    text-shadow: 1px 1px 2px #000;
    font-size: 48px;  /* Increased font size */
    padding: 20px;
}

.container-style {
    background-color: #ffffff;  /* White background for containers */
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);  /* Soft shadow effect */
    margin-bottom: 20px;
}

.button {
    background-color: #4CAF50; /* Green background */
    color: white;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    border-radius: 5px;
    transition: background-color 0.3s ease;
}

.button:hover {
    background-color: #45a049; /* Darker green on hover */
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)

# Create a container for the header
header_container = st.container()

# Create a container for the project title
title_container = st.container()

# Add a title with refined color, style, and effects
with title_container:
    st.markdown("""
    <h1 class="title-text">
    🕵️‍♂️ Online Payment Fraud Detection 🧧
    </h1>
    """, unsafe_allow_html=True)

def main():
    # List of images (you can replace these with your own image paths or URLs)
    images = [
        "bg15.jpg",
        "bg2.jpg",
        "bg4.jpg",
        "bg5.jpg",
        "bg9.jpg",
        "bg10.jpg",
        "bg11.jpg",
        "bg24.jpg",
        "bg1.jpg",
        "bg18.jpg",
        "bg19.jpg",
        
        "bg13.jpg",
        # Add more images as needed
    ]
    
    # Delay between slides (in seconds)
    delay = 2
    
    # Display area for the image
    image_placeholder = st.empty()
    
    # Add initial descriptive text
    st.markdown("<div class='container-style'>", unsafe_allow_html=True)
    st.title("Welcome to our Online Payment Fraud Detection project! 🎉")
    st.subheader("In today's digital world, the security of online transactions is paramount.")
    st.write("""
        Our project leverages advanced machine learning algorithms to detect fraudulent 
        transactions in real-time, ensuring a safe and secure payment experience for users. 
        By analyzing patterns and anomalies in transaction data, our system identifies potential 
        fraud with high accuracy and speed.
    """)
    st.write("""
        Key Features:
        - Real-time fraud detection
        - High accuracy and reliability
        - User-friendly interface
        - Scalable and robust architecture
    """)
    st.write("Join us in our mission to make online payments safer and more reliable. 💳🔒")
    st.markdown("</div>", unsafe_allow_html=True)
    
    i = 0
    while i < len(images):  # Loop until all images have been shown
        # Display the image
        image_placeholder.image(images[i], width=350, use_column_width=False, caption=f"Image {i+1}/{len(images)}")
        
        # Update descriptive text if needed (e.g., change every 3 images)
        if i % 3 == 0:
            st.write(f"Currently displaying Image {i+1}/{len(images)}")
        
        # Pause briefly before showing the next image
        time.sleep(delay)
        
        # Move to the next image in the list
        i += 1
    
    st.markdown("<div class='container-style'>", unsafe_allow_html=True)
     # Optional final message
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
