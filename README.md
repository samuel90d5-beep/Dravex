# Dravex – Personal AI Assistant (Phase 1–3)(DRAVEX BYE MAVLON)

Dravex is a Python-based personal assistant prototype.  
It can **speak, respond to text commands, and perform basic system tasks**.  
This is Phase 1–3 of development, laying the foundation for a future AI assistant.

---

## Features
- Greets you based on time of day (morning, afternoon, evening)
- Answers questions:
  - What is the time?
  - What is the date?
  - What is my name?
  - Who are you?
- Opens apps:
  - Calculator
  - Notepad
  - Chrome
  - Brave Browser
  - VS Code
  - Terminal
  - Wireshark
  - Arduino IDE
  - Spotify
  - File Explorer
- System control (with confirmation):
  - Shutdown
  - Restart
  - Sleep
- System info:
  - CPU usage
  - Memory usage
- Extra:
  - Greet me
  - Tell a random fact
  - Tell a random joke

---

##  Project Structure
Dravex/
│── main.py # Entry point
│── command_parser.py # Handles user commands
│── speech_engine.py # Text-to-speech engine
│── utils.py # Helper functions (time, date, system info)
│── commands.json # Stored command mappings
│── requirements.txt # Python dependencies
│── README.md # Project documentation