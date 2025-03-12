# 2️⃣ speech_to_text.py → Converts Game Audio to Text
# Uses Whisper AI (or another speech-to-text model)
# Example tasks:
# Listens to game sounds (e.g., player talking, announcer voice)
# Converts speech into text so AI can analyze it

import whisper

model = whisper.load_model("base")  # Load Whisper model

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]  # Returns transcribed text


