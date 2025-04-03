"""
Tool to analyze YouTube videos, making resumes and export to PDF
"""

# TODO: use whisper to transcribe audio and put it in a text file inside the "data"

# Import modules
import os
from pytubefix import YouTube
from pytubefix.cli import on_progress

from settings import get_downloads_path, get_data_path

try:
    print("Initializing...")
    import whisper
except ImportError:
    raise ImportError(
        "Whisper is not installed. Please install it using 'pip install whisper'."
    )


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


def get_audio_file():
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
            audio_file_path = os.path.join(
                get_downloads_path(), audio_files[file_index]
            )
            transcribe_audio(audio_file_path)
        else:
            print("Invalid choice.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return


def transcribe_audio(audio_file_path):
    # Load the Model
    model = whisper.load_model("medium")

    print(f"\nTranscribing: {audio_file_path}...\n")
    try:
        result = model.transcribe(audio_file_path)
        transcription_text = result["text"]

        file_name = os.path.splitext(os.path.basename(audio_file_path))[0] + ".txt"
        save_path = os.path.join(get_data_path(), file_name)

        with open(save_path, "w", encoding="utf-8") as f:
            f.write(transcription_text)
        print(f"Transcription saved to: {save_path}")
    except:
        print("Error transcribing audio, check audio file and try again")


def menu():
    print("1. Get video from URL")
    print("2. Transcribe audio")

    choice = input("Enter your choice: ")
    if choice == "1":
        get_video_from_url()
    elif choice == "2":
        get_audio_file()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    menu()
