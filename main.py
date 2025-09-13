from command_parser import handle_command
from utils import get_greeting
from speech_engine import speak

def main():
    print("|| DRAVEX BY MAVLON ||")
    greeting = f"{get_greeting()}, I am Dravex. How can I help you today?"
    print(f"Dravex: {greeting}")
    speak(greeting)

    while True:
        command = input("You: ").lower().strip()

        if command in ["exit", "quit", "close"]:
            farewell = "Goodbye! 👋"
            print(f"Dravex: {farewell}")
            speak(farewell)
            break

        response = handle_command(command)
        print(f"Dravex: {response}")
        speak(response)

if __name__ == "__main__":
    main()
