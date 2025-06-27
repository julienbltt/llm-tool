import pyttsx3

class _TTS:

    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 250) 

    def start(self,text_):
        self.engine.say(text_)
        self.engine.runAndWait()

tts = _TTS() # Initialize the tts engine

def talk(text: str):
    print(f"🎤 Vocal synthesis: {text}")
    tts.start(text)  