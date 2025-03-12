# 1️⃣ main.py → The Brain of Your AI System
# This is the entry point of your AI assistant.
# It calls all other modules to run the full AI pipeline.
# Example tasks in main.py:
# Capture game screenshots
# Convert game audio to text
# Store and retrieve relevant game knowledge

from speech_to_text import transcribe_audio
from game_capture import capture_screen
from game_context import get_game_advice, add_game_advice, game_memory
import os

# Disable TensorFlow Warnings
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Ensure game-related queries are filtered
def is_game_related(text):
    keywords = ["enemy", "movement", "attack", "strategy", "aim", "jump", "shoot"]
    return any(word in text.lower() for word in keywords)

# Adding game advice to memory
add_game_advice("Practice movement mechanics to outmaneuver opponents.")
add_game_advice("Adjust mouse sensitivity to improve aiming accuracy.")
add_game_advice("Learn enemy patterns to anticipate attacks.")

# Capture game screenshot
# screenshot_path = "assets/stare.png"
# capture_screen(screenshot_path)
# 🔹 Step 2: Use the Correct YouTube Window Title
capture_screen("assets/stare.png", "YouTube - Personal - Microsoft\u200b Edge")  # Replace with actual title

# Process game audio
audio_path = "assets/Tejo Bomb stuck valorant.mp3"
text = transcribe_audio(audio_path)

# Limit long text
max_chars = 150
text = text[:max_chars] + "..." if len(text) > max_chars else text

# Get AI advice
advice = get_game_advice(text) if is_game_related(text) else "No relevant game advice detected."

# Store the transcribed event if it's game-related
if text and text not in game_memory and is_game_related(text):
    add_game_advice(text)

print(f"Transcribed Text: {text}")
print(f"AI Advice: {advice}")
