import pyttsx3
import wikipedia

def speak(message):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate -10)
    engine.say('{}'.format(message))
    engine.runAndWait()

def my_summary():
    summ=wikipedia.summary('')
    return summ
 
val = my_summary()
speak(val)