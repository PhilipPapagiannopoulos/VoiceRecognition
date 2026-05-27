import pyttsx3
import time


def speak(mitsos,speed,voiceIndex):          #shift+tab  or  tab πολλέσ σειρές space
    engine = pyttsx3.init()

    rate = engine.getProperty('rate')
    engine.setProperty('rate', speed)

    engine.setProperty('volume', 1)

    fones = engine.getProperty('voices')
    if 0 <= voiceIndex <= len(fones):
        engine.setProperty('voice', fones[voiceIndex].id)


    engine.say(mitsos)
    engine.runAndWait()

engineTemp = pyttsx3.init()
fones = engineTemp.getProperty('voices')

print("Available voices:")
for i, v in enumerate(fones):
    print(i, v.name)


speed=int(input("Give me the speed(-50,50)"))
VoiceChoice = int(input("Give me a number for voice"))
set_chat=input("Give me a voice text")
speak(set_chat,speed,VoiceChoice)

#print("Voices found:", len(fones))
#for i, v in enumerate(fones):
      # print(i, v.name, "|", v.id)