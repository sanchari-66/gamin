#from speech_to_text import transcribe_audio

#audio_path = "assets/everything.mp3"  # Replace with your own file path
#text = transcribe_audio(audio_path)
#print(f"Transcribed Text: {text}")

# so output shoild be like this -"[Running] python -u "c:\Users\basin\Dropbox\timepass\game_ai_project\test.py"
#C:\Users\basin\AppData\Local\Programs\Python\Python312\Lib\site-packages\whisper\transcribe.py:126: UserWarning: FP16 is not supported on CPU; using FP32 instead
# warnings.warn("FP16 is not supported on CPU; using FP32 instead")
#Transcribed Text:  I had a dream, I got everything I wanted, I thought I could fly, so I stepped off the golden, nobody cried, so anyone who might care, but I could fly, so I stepped off the golden, nobody cried, nobody even noticed I saw them standing right there, kinda thought they might care, I had a dream, I got everything I wanted, but when I wake up I see, you're with me, and you say as long as I'm here, no one can hurt you, don't wanna lie here, but you can learn too, if I could tie you to a way you'd just see, so you wouldn't wanna lie here, they don't deserve you, I tried to scream, but my head was under water, they called me weak, I come not just somebody's daughter, it could have been a nightmare, but it felt like they were right there, and it feels like yesterday was a year ago, well I don't wanna let anybody know, cause everybody wants something from me now, and I don't wanna let them down, I had a dream, I got everything I wanted, but when I wake up I see, you're with me, and you say as long as I'm here, no one can hurt you, don't wanna lie here, but you can learn too, if I could tie you to a way you'd just see, so you wouldn't wanna lie here, they don't deserve you, if I could move it all then, what I do, what I do, what I do, what I do, what I do, if I could tie you to a way you'd just see, so you wouldn't tell me how you'd do, what you'd just see, so you wouldn't tell me how you'd do, if I could tie you to a way you'd just see, so you'd let anybody know,
#"

# Test game capture.personality
#from game_capture import capture_screen

#output_path = 'assets/stare.png'  # Set your desired screenshot location
#capture_screen(output_path)

# output : screenshot of this tab would be in stare.png

# Test game_context.get_game_advice

from game_context import store_game_memory, get_game_advice

# Store some game advice
store_game_memory("Use your special move when enemy is near.")

# Retrieve the stored advice
advice = get_game_advice("When should I attack?")
print(f"AI Advice: {advice}")

# output :
# [Running] python -u "c:\Users\basin\Dropbox\timepass\game_ai_project\test.py"
#2025-03-11 21:43:13.341584: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
#2025-03-11 21:43:22.958203: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
#Traceback (most recent call last):