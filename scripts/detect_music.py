# scripts/detect_music.py
import librosa
import numpy as np

def detect_music_segments(audio_path):
    y, sr = librosa.load(audio_path)
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)
    onset_times = librosa.frames_to_time(onset_frames, sr=sr)

    music_segments = []
    for onset in onset_times:
        start = float(onset)
        end = min(float(onset + 5), librosa.get_duration(y=y, sr=sr))
        music_segments.append((start, end))
    
    return music_segments

def save_segments_to_file(segments, file_path):
    with open(file_path, 'w') as file:
        for start, end in segments:
            file.write(f"{start},{end}\n")

if __name__ == "__main__":
    audio_path = r"C:\Users\auddy\Music\output_audio.mp3"
    segments_file = r"C:\Users\auddy\Music\music_segments.txt"
    music_segments = detect_music_segments(audio_path)
    save_segments_to_file(music_segments, segments_file)
    print(f"Detected music segments saved to {segments_file}")
