# THE PROGRAM MIGHT TAKE A FEW MINUTES TO RUN OR SOMETIMES A FEW SECONDS - IT DEPENDS ON YOUR COMPUTER'S SPEED 
import pyttsx3
import wikipedia

def speak(message):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate -10)
    engine.say('{}'.format(message))
    engine.runAndWait()

def my_summary():
    summ=wikipedia.summary('TYPE IN YOUR WHAT YOU WANT TO SEARCH HERE - NOTE - THE TOPIC MUST BE DOCUMENTED  BY WIKIPEDIA FOR THE PROGRAM TO WORK  ')
    return summ
 
val = my_summary()
speak(val)
