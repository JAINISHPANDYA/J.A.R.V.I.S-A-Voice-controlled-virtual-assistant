import speech_recognition as sr 
import pyttsx3 


engine = pyttsx3.init()

rate = engine.getProperty("rate")
print(rate)

engine.setProperty("rate", 150)

voices = engine.getProperty("voices")


engine.setProperty("voice", voices[1].id)






engine.say("whats your name")
engine.runAndWait()




r = sr.Recognizer()
print("listenning")
with sr.Microphone() as source:
    
    audio= r.listen(source)
    text  = r.recognize_google(audio)

    engine.say("hello" + text)
    engine.runAndWait()
    engine.say("this is jarvis  how can i help you")
    engine.runAndWait()
   

 


      



    
