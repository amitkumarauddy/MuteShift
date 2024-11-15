import subprocess

def extract_audio_ffmpeg(video_path, output_audio_path):
    """
    Extracts audio from a video file using FFmpeg.

    Parameters:
        video_path (str): Path to the input video file.
        output_audio_path (str): Path to save the extracted audio file.
    """
    try:
        # Use FFmpeg to extract audio
        command = [
            "ffmpeg", "-y",           # Overwrite output if it exists
            "-i", video_path,         # Input video file
            "-vn",                    # Skip the video stream
            "-acodec", "mp3",         # Output audio codec
            output_audio_path         # Output audio file
        ]
        subprocess.run(command, check=True)
        print(f"Audio extracted and saved as {output_audio_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error while extracting audio: {e}")

if __name__ == "__main__":
    video_path = r"C:\Users\auddy\Videos\input_video.mp4"  # Input video path
    output_audio_path = r"C:\Users\auddy\Music\output_audio.mp3"  # Output audio path
    extract_audio_ffmpeg(video_path, output_audio_path)
