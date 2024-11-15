# scripts/detect_music.py
import librosa
import numpy as np

def detect_music_segments(audio_path):
    # Load the audio file
    y, sr = librosa.load(audio_path)
    
    # Analyze the onset (beginning) of sounds
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    
    # Convert frames to time
    onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)
    onset_times = librosa.frames_to_time(onset_frames, sr=sr)

    # Create music segments based on onset times
    music_segments = []
    for onset in onset_times:
        # Example: Create a segment of 5 seconds from each onset time
        start = float(onset)
        end = min(float(onset + 5), librosa.get_duration(y=y, sr=sr))
        music_segments.append((start, end))
    
    return music_segments

if __name__ == "__main__":
    audio_path = r"C:\Users\auddy\Music\output_audio.mp3"  # Path to the extracted audio file
    music_segments = detect_music_segments(audio_path)
    print("Detected music segments:")
    for segment in music_segments:
        print(f"Start: {segment[0]:.2f}s, End: {segment[1]:.2f}s")
