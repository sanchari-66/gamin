# 3️⃣ game_capture.py → Captures Game Screen for AI
# Uses OpenCV to take screenshots of the game
# Can process images to detect key elements
# Optional: Use OCR (Optical Character Recognition) to extract text from the screen

import pygetwindow as gw
import pyautogui
import time

def capture_screen(file_path, window_title):
    # Get the YouTube game window
    game_window = None
    for window in gw.getWindowsWithTitle(window_title):
        if window_title in window.title:
            game_window = window
            break

    if game_window:
        # Bring the window to the front
        game_window.activate()
        time.sleep(2)  # Allow time for the window to focus

        # Capture only the game window region
        left, top, width, height = game_window.left, game_window.top, game_window.width, game_window.height
        screenshot = pyautogui.screenshot(region=(left, top, width, height))
        screenshot.save(file_path)
        print(f"Screenshot saved successfully at {file_path}")
    else:
        print(f"Window '{window_title}' not found.")

# 🔹 Step 1: Check Available Windows
print("Available Windows: ", gw.getAllTitles())  

