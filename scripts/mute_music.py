# scripts/mute_music.py
from moviepy.editor import VideoFileClip, AudioFileClip

def combine_video_audio(video_path, audio_path, output_path):
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)
    video = video.set_audio(audio)
    video.write_videofile(output_path, audio_codec='aac')
    print(f"Video with muted audio saved as {output_path}")

if __name__ == "__main__":
    video_path = r"C:\Users\auddy\Videos\input_video.mp4"
    muted_audio_path = r"C:\Users\auddy\Music\muted_audio.mp3"
    output_video_path = r"C:\Users\auddy\Videos\muted_video.mp4"

    combine_video_audio(video_path, muted_audio_path, output_video_path)
