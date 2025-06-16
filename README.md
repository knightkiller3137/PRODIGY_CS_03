# PRODIGY_CS_03
# 🛡️ My_Keylogger – Python Keylogger (Educational Use)

**My_Keylogger** is a basic Python-based keylogger built for educational and ethical cybersecurity training. It logs every key pressed by the user and records them in a timestamped log file. This project uses the [`pynput`](https://pypi.org/project/pynput/) library to listen to keyboard events in real-time.

> 🚨 **This project is intended strictly for educational purposes only. Unauthorized use is illegal and unethical.**

---

## 📁 Project Files

- `My_Keylogger.py` – The main keylogger script
- `keylog.txt` – Automatically created to store the logged keystrokes
- `README.md` – You're reading it

---

## 🚀 How It Works

1. Listens for keyboard events using `pynput.keyboard`.
2. Captures both character keys and special keys (like `[enter]`, `[esc]`, `[space]`).
3. Logs each keystroke along with the current timestamp.
4. Stops logging when the **ESC key** is pressed.

---

## 🖥️ How to Run

### 🧩 Prerequisites
- OS: Windows
- Python 3.6 or higher installed
- Internet access to install `pynput` if not already installed

### 📦 Install Dependencies
Open Command Prompt or PowerShell and run:

<pre>bash
pip install pynput</pre>

## ▶️ Run the Script
Navigate to the folder where My_Keylogger.py is saved and run:

<pre>bash
python My_Keylogger.py</pre>
You’ll see:

<pre>vbnet
Starting keylogger... (Press ESC to stop)</pre>
Once ESC is pressed, logging stops and all keystrokes are saved to `keylog.txt`

## 📄 Sample Output (keylog.txt)
<pre>yaml
2025-06-06 21:15:03 - h
2025-06-06 21:15:04 - e
2025-06-06 21:15:05 - l
2025-06-06 21:15:06 - l
2025-06-06 21:15:07 - o
2025-06-06 21:15:08 - [space]
2025-06-06 21:15:09 - w
2025-06-06 21:15:10 - o
2025-06-06 21:15:11 - r
2025-06-06 21:15:12 - l
2025-06-06 21:15:13 - d </pre>
## ⚠️ Legal & Ethical Disclaimer
This tool is created for:
-Cybersecurity practice
-Ethical hacking labs
-Education on input monitoring and Python automation
-Do NOT use this tool on devices or users without their clear and informed consent. Unauthorized monitoring or keylogging is illegal under laws like the Computer Fraud and Abuse Act (CFAA).

## 📚 Skills & Concepts Used
-Python scripting
-Event listeners (pynput)
-File I/O operations
-Keyboard automation
-Ethical considerations in cybersecurity

## 👨‍💻 Author
### Manik Chand Singh
Cybersecurity enthusiast | Python beginner | Ethical hacker-in-training
