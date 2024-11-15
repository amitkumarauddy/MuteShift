# scripts/detect_and_mute_music.py
import librosa
import numpy as np
import soundfile as sf

def detect_music_segments(audio_path, threshold=0.02, frame_duration=1, min_duration=5):
    """
    Detects music segments with energy above a threshold and longer than a specified duration.

    Parameters:
        audio_path (str): Path to the input audio file.
        threshold (float): RMS energy threshold to detect music.
        frame_duration (float): Duration of each frame in seconds.
        min_duration (float): Minimum duration for a segment to be considered music (in seconds).

    Returns:
        List[Tuple[float, float]]: Start and end times of detected music segments.
    """
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
                if end - start >= min_duration:  # Check if segment duration exceeds min_duration
                    music_segments.append((start, end))
                start = None

    # Handle last segment if it goes till the end of the audio
    if start is not None and times[-1] - start >= min_duration:
        music_segments.append((start, times[-1]))

    return music_segments

def mute_segments(audio_path, output_path, segments):
    """
    Mutes the specified segments in an audio file.

    Parameters:
        audio_path (str): Path to the input audio file.
        output_path (str): Path to save the output audio file.
        segments (List[Tuple[float, float]]): Start and end times of segments to mute.
    """
    y, sr = librosa.load(audio_path, sr=None)
    audio_length = len(y) / sr
    segment_samples = [(int(start * sr), int(end * sr)) for start, end in segments]

    # Create a copy of the audio signal
    muted_audio = np.copy(y)

    for start_sample, end_sample in segment_samples:
        muted_audio[start_sample:end_sample] = 0  # Mute the segment

    # Save the modified audio
    sf.write(output_path, muted_audio, sr)

if __name__ == "__main__":
    audio_path = r"C:\Users\auddy\Music\output_audio.mp3"
    output_path = r"C:\Users\auddy\Music\muted_audio.mp3"
    segments_file = r"C:\Users\auddy\Music\music_segments.txt"

    # Detect music segments
    music_segments = detect_music_segments(audio_path, min_duration=5)
    print(f"Detected music segments longer than 5 seconds: {music_segments}")

    # Save segments to a file
    with open(segments_file, 'w') as file:
        for start, end in music_segments:
            file.write(f"{start},{end}\n")

    print(f"Detected music segments saved to {segments_file}")

    # Mute the detected segments
    mute_segments(audio_path, output_path, music_segments)
    print(f"Muted audio saved to {output_path}")
