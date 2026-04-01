import yt_dlp, os
import streamlit as st

st.title("🎬 YouTube Video Downloader")

url = st.text_input("Enter YouTube URL:")
path = st.text_input("Save Location:", value=os.path.join(os.path.expanduser("~"), "Downloads", "YouTube_Videos"))

if st.button("Download"):
    if not url:
        st.warning("Please enter a YouTube URL!")
    else:
        with st.spinner("Downloading..."):
            try:
                os.makedirs(path, exist_ok=True)
                ydl_opts = {
                    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                    'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
                    'merge_output_format': 'mp4',
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                saved = os.path.join(path, info['title'] + '.mp4')
                st.success(f"✅ Download Complete!")
                st.info(f"📂 Saved at: {saved}")
            except Exception as e:
                st.error(f"❌ Error: {e}")
