# 2️⃣ speech_to_text.py → Converts Game Audio to Text
# Uses Whisper AI (or another speech-to-text model)
# Example tasks:
# Listens to game sounds (e.g., player talking, announcer voice)
# Converts speech into text so AI can analyze it

import whisper
import torch
from pydub import AudioSegment, silence

# Load Whisper model (use GPU if available)
if torch.cuda.is_available():
    model = whisper.load_model("base").to("cuda")
else:
    model = whisper.load_model("base")

# Function to trim silence from the audio
def trim_silence(audio_path):
    audio = AudioSegment.from_file(audio_path)
    non_silent = silence.detect_nonsilent(audio, min_silence_len=500, silence_thresh=-40)
    if not non_silent:
        return audio_path  # No trimming needed

    start, end = non_silent[0][0], non_silent[-1][1]
    trimmed_audio = audio[start:end]
    trimmed_audio.export(audio_path, format="mp3")
    return audio_path

# Function to transcribe audio with deterministic output
def transcribe_audio(audio_path):
    audio_path = trim_silence(audio_path)  # Trim silence before transcription
    result = model.transcribe(audio_path, temperature=0, language="en")  # Make transcription deterministic
    return result["text"]  # Returns transcribed text
