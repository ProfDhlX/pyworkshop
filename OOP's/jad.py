import pyttsx3
engine = pyttsx3.init()
text = "tintililililililililililililililililillilililitintililililililililillililililililil"

engine.setProperty('rate', 150)   
engine.setProperty('volume', 0.9)

engine.say(text)
engine.runAndWait()