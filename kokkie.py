import pyttsx3
import speech_recognition as sr
import webbrowser 
import datetime 
import wikipedia
import pyaudio
import youtube
 
def takeCommand():
 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
         
        r.pause_threshold = 0.7
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
        
        try:
            print("Recognizing....")
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed={}".format(Query))
             
        except Exception as e:
            print(e)
            print("Say that again please")
            return "None"
         
        return Query
 
def speak(audio):
     
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    
    engine.runAndWait()
 
def tellDay():
     
 
    day = datetime.datetime.today().weekday() + 1
     
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
     
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)
 
 
def tellTime(self):
     
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    self.speak(self, "The time is " + hour + "Hours and" + min + "Minutes")   
 
def Hello():
     
    speak("Hello My name is Kookie ,I am your desktop assistant. Tell me how may I help you")
 
 
def Take_query():

    Hello()
    while(True):
        
        query = takeCommand().lower()
        if "open GeekeforGeeks" in query:
            speak("Opening GeeksfoeGeeks ")
            webbrowser.open("www.geeksforgeeks.com")
            continue
        
        elif "hello" in query:
            speak("Hello,I hope you are having a good day. How may I help you.")
         
        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("www.google.com")
            continue
        elif "open youtube" in query:
            speak("Opening Youtube")
            webbrowser.open("https://www.youtube.com/")
            continue
        
        elif " in google" in query:
            speak("searching in google")
            webbrowser.open
             
        elif "which day it is" in query:
            tellDay()
            continue
         
        elif "tell me the time" in query:
            tellTime()
            continue
         
        elif "bye" in query:
            speak("It was nice to help.Bye")
            exit()
         
        elif "from wikipedia" in query:
             
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")
             
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)
            
        elif "from youtube" in query:
             
            speak("opening from youtube ")
            query = query.replace("youtube", "")
             
            result =youtube.summary(query, sentences=4)
            speak("Opening youtube")
            speak(result)
         
        elif "What is your name" in query:
            speak("I am Kookie. Your desktop Assistant")
 
if __name__ == '__main__':
     
    Take_query()