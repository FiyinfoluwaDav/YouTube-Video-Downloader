import os
import yt_dlp

# Ask user for video URL
video_url = input("Enter the YouTube video URL: ")

# Create downloads folder if it doesn't exist
os.makedirs("videos", exist_ok=True)

# yt-dlp options
ydl_opts = {
    'outtmpl': 'videos/%(title)s.%(ext)s',  # save video inside 'downloads' folder
    'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',  # download up to 720p
    'merge_output_format': 'mp4',  # final format mp4
}

# Download video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print("✅ Video downloaded at 720p (or best available <=720p)!")
