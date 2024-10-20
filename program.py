import streamlit as st
import yt_dlp

# Set up the Streamlit app
st.title("YouTube Video Downloader")

# Input for the YouTube URL
video_url = st.text_input("Enter the YouTube Video URL:")

if st.button("Download"):
    if video_url:
        # Define a callback function to show progress
        progress_placeholder = st.empty()  # Create a placeholder for the progress bar

        def progress_hook(d):
            if d['status'] == 'downloading':
                # Calculate the progress percentage
                percent = d['downloaded_bytes'] / d['total_bytes']
                progress_placeholder.progress(percent)  # Update the progress bar
            elif d['status'] == 'finished':
                progress_placeholder.success(f"Download completed: {d['filename']}")

        try:
            # Set the download options with fixed resolution at 720p
            ydl_opts = {
                'format': 'bestvideo[height<=720]+bestaudio/best',  # Fixed to 720p
                'outtmpl': '%(title)s.%(ext)s',  # Output file name format
                'progress_hooks': [progress_hook],
            }

            # Use yt_dlp to download the video
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(video_url, download=True)
                video_title = info_dict.get('title', None)
                st.success(f"Downloaded: {video_title}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter a valid URL.")
