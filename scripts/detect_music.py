# scripts/detect_music.py
import librosa
import numpy as np

def detect_music_segments(audio_path, threshold=0.02, frame_duration=1):
    # Load the audio file
    y, sr = librosa.load(audio_path)
    
    # Calculate the root mean square (RMS) energy for each frame
    frame_length = int(frame_duration * sr)
    hop_length = frame_length
    rms_energy = librosa.feature.rms(y=y, frame_length=frame_length, hop_length=hop_length)[0]

    # Calculate times for frames
    times = librosa.frames_to_time(range(len(rms_energy)), sr=sr, hop_length=hop_length)
    
    # Detect segments with energy above the threshold
    music_segments = []
    start = None
    for t, e in zip(times, rms_energy):
        if e > threshold:
            if start is None:
                start = t
        else:
            if start is not None:
                end = t
                music_segments.append((start, end))
                start = None

    # Handle last segment if it goes till the end of the audio
    if start is not None:
        music_segments.append((start, times[-1]))

    return music_segments

def save_segments_to_file(segments, file_path):
    with open(file_path, 'w') as file:
        for start, end in segments:
            file.write(f"{start},{end}\n")

if __name__ == "__main__":
    audio_path = "../audio/output_audio.mp3"
    segments_file = "../audio/music_segments.txt"
    music_segments = detect_music_segments(audio_path)
    save_segments_to_file(music_segments, segments_file)
    print(f"Detected music segments saved to {segments_file}")
