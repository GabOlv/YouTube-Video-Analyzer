"""
Tool to analyze YouTube videos, making resumes and export to PDF
"""

# TODO: use whisper to transcribe audio and put it in a text file inside the "data"

# Import modules
import os
from pytubefix import YouTube
from pytubefix.cli import on_progress

from settings import get_downloads_path

# import whisper


def get_video_from_url():
    # Get URL:
    video_url = input("Enter video URL: ")
    youtube_video = YouTube(video_url, on_progress_callback=on_progress)

    try:
        youtube_streams = youtube_video.streams.get_audio_only()
        youtube_streams.download(output_path=get_downloads_path())
    except:
        print("Error downloading video, check URL, internet connection and try again")

    choice = input("Want to transcribe audio? (y/n): ")
    if choice == "y":
        transcribe_audio()
    else:
        menu()


def transcribe_audio():
    audio_files = [
        audio_file
        for audio_file in os.listdir(get_downloads_path())
        if audio_file.endswith((".m4a", ".mp3"))
    ]

    if not audio_files:
        print("No audio files found in the downloads folder.")
        return

    # Display the list of audio files
    print("\nAudio files found in the downloads folder:")
    for i, audio_file in enumerate(audio_files, 1):
        print(f"{i}. {audio_file}")

    try:
        file_index = int(input("\nEnter the number of the audio file: ")) - 1
        if 0 <= file_index < len(audio_files):
            selected_file = os.path.join(get_downloads_path(), audio_files[file_index])
        else:
            print("Invalid choice.")
            return  # Exit function if the choice is invalid
    except ValueError:
        print("Invalid input. Please enter a number.")
        return


def menu():
    print("1. Get video from URL")
    print("2. Transcribe audio")

    choice = input("Enter your choice: ")
    if choice == "1":
        get_video_from_url()
    elif choice == "2":
        transcribe_audio()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    menu()
