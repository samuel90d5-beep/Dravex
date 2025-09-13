import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 170)  
engine.setProperty("volume", 1.0)  
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id) 

def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"TTS Error: {e}")
