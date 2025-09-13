import os
import webbrowser
import psutil
import datetime
from utils import get_greeting

USER_NAME = "Sammy"  

def handle_command(command):
    
    if "hello" in command or "hi" in command:
        return f"{get_greeting()}, {USER_NAME}!"

    
    elif "who are you" in command or "what are you" in command:
        return "I am Dravex, your personal AI assistant."

    
    elif "my name" in command:
        return f"Your name is {USER_NAME}."


    elif "time" in command:
        return f"The time is {datetime.datetime.now().strftime('%H:%M:%S')}."

    
    elif "date" in command:
        return f"Today is {datetime.datetime.now().strftime('%A, %B %d, %Y')}."

    
    elif "battery" in command:
        battery = psutil.sensors_battery()
        if battery:
            return f"Battery is at {battery.percent}%."
        return "Battery info not available."

    
    elif "open calculator" in command:
        os.system("gnome-calculator &")
        return "Opening Calculator..."

    elif "open note" in command:
        os.system("xed &")  
        return "Opening Notes..."

    elif "open chrome" in command:
        os.system("google-chrome &")
        return "Opening Google Chrome..."

    elif "open brave" in command:
        os.system("brave-browser &")
        return "Opening Brave Browser..."

    elif "open vs code" in command:
        os.system("code &")
        return "Opening Visual Studio Code..."

    elif "open terminal" in command:
        os.system("gnome-terminal &")
        return "Opening Terminal..."

    elif "open wireshark" in command:
        os.system("wireshark &")
        return "Opening Wireshark..."

    elif "open arduino" in command:
        os.system("arduino &")
        return "Opening Arduino IDE..."

    elif "open spotify" in command:
        os.system("spotify &")
        return "Opening Spotify..."

    elif "open folder" in command:
        os.system("xdg-open ~ &")
        return "Opening Home Folder..."

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube..."

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google..."

    
    elif "shutdown" in command:
        confirm = input("Dravex: Are you sure you want to shutdown? (yes/no): ").lower()
        if confirm == "yes":
            os.system("shutdown now")
            return "Shutting down..."
        else:
            return "Shutdown cancelled."

    elif "restart" in command:
        confirm = input("Dravex: Are you sure you want to restart? (yes/no): ").lower()
        if confirm == "yes":
            os.system("reboot")
            return "Restarting system..."
        else:
            return "Restart cancelled."

    elif "sleep" in command:
        confirm = input("Dravex: Put system to sleep? (yes/no): ").lower()
        if confirm == "yes":
            os.system("systemctl suspend")
            return "System going to sleep..."
        else:
            return "Sleep cancelled."

    
    elif "weather" in command:
        return "I cannot fetch weather yet, but that’s coming in Phase 2."

    elif "joke" in command:
        return "Why did the computer show up at work late? It had a hard drive."

    elif "cpu usage" in command:
        return f"CPU usage is {psutil.cpu_percent()}%."

    elif "memory usage" in command:
        mem = psutil.virtual_memory()
        return f"Memory usage is {mem.percent}%."

    elif "greet me" in command:
        return f"{get_greeting()}, {USER_NAME}!"

    else:
        return "Sorry, I don’t understand that yet."
