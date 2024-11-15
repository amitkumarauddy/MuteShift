# scripts/extract_audio.py
from moviepy.editor import VideoFileClip

def extract_audio(video_path, output_audio_path):
    # Load the video file
    video = VideoFileClip(video_path)
    
    # Extract the audio from the video
    audio = video.audio
    
    # Save the audio to a file
    audio.write_audiofile(output_audio_path)
    print(f"Audio extracted and saved as {output_audio_path}")

if __name__ == "__main__":
    video_path = r"C:\Users\auddy\Videos\input_video.mp4"  # Update with your video path
    output_audio_path = r"C:\Users\auddy\Music\output_audio.mp3"  # Output audio path
    extract_audio(video_path, output_audio_path)
