# 3️⃣ game_capture.py → Captures Game Screen for AI
# Uses OpenCV to take screenshots of the game
# Can process images to detect key elements
# Optional: Use OCR (Optical Character Recognition) to extract text from the screen

import sys
sys.stdout.reconfigure(encoding='utf-8')

import pygetwindow as gw
import pyautogui
import time
import re


windows = gw.getAllTitles()
for title in windows:
    print(title)

def clean_window_title(title):
    """Removes invisible Unicode characters from window titles."""
    title = re.sub(r'[\u200b\u202a\u202c]', '', title)  # Remove zero-width characters
    title = re.sub(r' - Personal - Microsoft Edge$', '', title)  # Remove Edge extra text
    return title.strip()

def find_game_window():
    """Finds the correct game window."""
    game_keywords = ["Valorant", "CSGO", "Apex", "Counter-Strike", "Call of Duty"]
    windows = gw.getAllTitles()

    for window in windows:
        if any(keyword.lower() in window.lower() for keyword in game_keywords):
            return window  # Return the first matching game window

    return None  # No game window found

def focus_window(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    if not windows:
        print(f"❌ Window '{window_title}' not found.")
        return False
    try:
        windows[0].activate()
        return True
    except Exception:
        pyautogui.moveTo(windows[0].left + 50, windows[0].top + 50)
        pyautogui.click()
        return True



import mss

def capture_screen(file_path, window_title):
    """Captures a screenshot using mss (better for games)."""
    if not window_title:
        print("❌ No game window found.")
        return

    if not focus_window(window_title):  # Try to focus window first
        print(f"⚠️ Could not focus on {window_title}. Screenshot may be incorrect.")

    with mss.mss() as sct:
        sct.shot(output=file_path)  # Capture entire screen
        print(f"✅ Screenshot saved at {file_path}")
