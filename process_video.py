import subprocess
import os

files = os.listdir("videos")
for file in files:
    subprocess.run(["ffmpeg","-i",f"videos/{file}",f"audios/{file}.mp3"])
