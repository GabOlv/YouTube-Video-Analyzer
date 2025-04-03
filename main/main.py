"""
Tool to analyze YouTube videos, making resumes and export to PDF
"""

# TODO: Import youtube URL and extract it audio to use with OpenAI Whisper
# Import modules

from pytubefix import YouTube
from pytubefix.cli import on_progress

from settings import get_downloads_path

# Get URL:
video_url = input("Enter video URL: ")
youtube_video = YouTube(video_url, on_progress_callback=on_progress)
print(youtube_video.title)

youtube_streams = youtube_video.streams.get_audio_only()
youtube_streams.download(output_path=get_downloads_path())
