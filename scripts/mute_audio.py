# scripts/mute_audio.py
from pydub import AudioSegment

def mute_audio_segments(audio_path, segments, output_path):
    audio = AudioSegment.from_file(audio_path)

    for start, end in segments:
        start_ms = int(start * 1000)
        end_ms = int(end * 1000)
        audio = audio[:start_ms] + AudioSegment.silent(duration=(end_ms - start_ms)) + audio[end_ms:]

    audio.export(output_path, format="mp3")
    print(f"Muted audio saved as {output_path}")

def load_segments_from_file(file_path):
    segments = []
    with open(file_path, 'r') as file:
        for line in file:
            start, end = map(float, line.strip().split(','))
            segments.append((start, end))
    return segments

if __name__ == "__main__":
    audio_path = r"C:\Users\auddy\Music\output_audio.mp3"
    segments_file = r"C:\Users\auddy\Music\music_segments.txt"
    output_audio_path = r"C:\Users\auddy\Music\muted_audio.mp3"

    music_segments = load_segments_from_file(segments_file)
    mute_audio_segments(audio_path, music_segments, output_audio_path)
