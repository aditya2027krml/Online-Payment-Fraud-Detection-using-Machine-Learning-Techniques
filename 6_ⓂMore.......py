import os
import streamlit as st
import time

# Set the image folder path
image_folder = r"Images/Images_More"

# Set the video folder path
video_folder = r"videos"

# Get a list of all image files in the folder
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.gif','jfif'))]

# Get a list of all video files in the folder
video_files = [f for f in os.listdir(video_folder) if f.endswith(('.mp4', '.avi', '.mov', '.mkv'))]

# Create a Streamlit container to hold the images and videos
st.set_page_config(page_title="Media Gallery", page_icon=":frame_photo:", layout="wide")

# Add a title
st.title("Media Gallery")
st.write("")

# Add a progress bar
progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)
    time.sleep(0.01)

# Display all images in the folder
st.header("Images")
cols = st.columns(3)  # 3 columns per row
for i, image_file in enumerate(image_files):
    cols[i % 3].image(os.path.join(image_folder, image_file), use_column_width=True, caption=image_file)

# Display all videos in the folder
st.header("Videos")
for video_file in video_files:
    st.video(os.path.join(video_folder, video_file), format="video/mp4")

# Add a footer
st.write("")
st.write("**Note:** USE ⬛ BLACK THEMED APPLICATION, IT WILL GIVE MORE ELEGANT LOOK !")