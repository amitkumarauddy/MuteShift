import subprocess

def combine_video_audio_ffmpeg(video_path, audio_path, output_path):
    """
    Combines a video file with an audio file using FFmpeg without re-encoding the video stream.
    Ensures only the new audio is included.
    """
    try:
        # Use FFmpeg to merge the video and audio
        command = [
            "ffmpeg", "-y",  # Overwrite output if it exists
            "-i", video_path,  # Input video file
            "-i", audio_path,  # Input audio file
            "-map", "0:v:0",  # Select the video stream from the first input
            "-map", "1:a:0",  # Select the audio stream from the second input
            "-c:v", "copy",   # Copy the video stream (no re-encoding)
            "-c:a", "aac",    # Encode audio as AAC
            output_path       # Output file
        ]
        subprocess.run(command, check=True)
        print(f"Video with muted audio saved as {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error while merging video and audio: {e}")

if __name__ == "__main__":
    video_path = r"C:\Users\auddy\Videos\input_video.mp4"
    muted_audio_path = r"C:\Users\auddy\Music\muted_audio.mp3"
    output_video_path = r"C:\Users\auddy\Videos\muted_video.mp4"

    combine_video_audio_ffmpeg(video_path, muted_audio_path, output_video_path)
