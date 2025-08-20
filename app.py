import os
import yt_dlp
from flask import Flask, request, render_template, send_file

app = Flask(__name__)

# Ensure downloads folder exists
os.makedirs("videos", exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        resolution = request.form["resolution"]

        # Output template
        output_file = "videos/%(title)s.%(ext)s"

        # yt-dlp options
        ydl_opts = {
            'outtmpl': output_file,
            'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
            'merge_output_format': 'mp4',
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
                filename = filename.replace(".webm", ".mp4")  # ensure mp4

            return send_file(filename, as_attachment=True)

        except Exception as e:
            return f"❌ Error: {str(e)}"

    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)
