import webbrowser #for opening webbrowser
import pyttsx3 #for speaking jenny
import datetime #for date and time
import speech_recognition as sr  #for speech recognition
import wikipedia   #for wikipedia function
import os  #to perform os function like opening software


engine = pyttsx3.init('sapi5')  # google it : sapi5 is a voice api provided my microsoft which provide voice functionality to our program.
                                # setting voice property to engine
voices = engine.getProperty('voices')
#print(voices[1].id)   #shows which voice we are using
engine.setProperty('voice',voices[1].id)      #set voice property to id 1

#functiion that let jenny speak

def speak(audio):
    engine.say(audio)  #makes the engine say
    engine.runAndWait() #runAndWait() python speech recognition” Code Answer's. engine. say("I am the text spoken after changing the speech rate.")

#code to wsh on starting

def WishMe():
    speak(" hello Manas")  # calling speak function
    hour = int(datetime.datetime.now().hour) #gives hour 0-24
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good AfterNooon!")
    else:
        speak("Good Evening!")
    speak("It's Jenny here.")

#takes command from microphone

def takeCommands():
    r=sr.Recognizer()            #set a variable to use sr 
    with sr.Microphone() as source:     #set microphone as source of input 
        print("Listening...")       #tells it's listenting
        r.pause_threshold = 0.8      #this increase the duration of pause to 1s so that is we take a long pause it don't disconnect
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in' )
        print(query)
        
    except Exception as e:
        print(e)
        print("Say that again please....")
        return "None"
    
    return query

#code for google search

def googleSearch(str):
    taburl = "https://google.com/search?q="
    search = taburl + query
    search = search.replace(' ', "+")
    print("Searching the url : ", search)
    webbrowser.get('chrome').open_new(search)


#code for opning and closing a file
def osfunc(str):
    print(query)
    if 'open' in query:
        os.startfile(str)
    if ' close' in query:
        print("coming soon....")



#Registering chrome browser
webbrowser.register('chrome', None ,
webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))




if __name__ == "__main__":

    WishMe()  #wishing function

#for listening continously

    while True:
        query = takeCommands().lower()

        #logic for executing tasks based on query

       # if 'jenny' in query or 'open' in query:
        query = query.replace('jenny', " ")

        if 'what is' in query:  # searching in wikipedia
            try:
                speak('Searching...')
                query = query.replace('what is', " ")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)  # prints wikipedia result
                speak(results)  # reads wikipedia result
                speak("Showing, google result for reference")
                googleSearch(query)  # showing google result after wikipedia

            except Exception as e:  # shows google results if wikipedia fails
                print(e)
                speak("Showing google search result...")
                googleSearch(query)

        elif 'open youtube' in query:  # opening youtube
            speak("opening youtube")
            webbrowser.get('chrome').open_new("youtube.com")

        elif 'search' in query:  # searching in google
            speak("searching in Google..")
            query = query.replace('search', "")
            googleSearch(query)

        elif 'my song' in query:  # playing kids in youtube
            speak("Playing Kids! By, One republic....... Enjoy! ")
            webbrowser.get('chrome').open("https://youtu.be/Y56lpXvXbs0")

        elif 'coding lectures' in query:  # playing kids in youtube
            speak("Opening, your comp playlist in youtube.....")
            webbrowser.get('chrome').open(
                "https://www.youtube.com/playlist?list=PLBcrgzXdWZ0S6lCaEGfVMnfaeU6qSd4OP")

        # code to open some softwares

        elif 'open vs code' in query:
            VSpath = "C:\Microsoft VS Code\Code.exe"
            osfunc(VSpath)

        elif 'open WhatsApp' in query:
            WApath = "C:\\Users\\Manas\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            osfunc(WApath)

        elif 'open photoshop' in query:
            PSpath = "C:\Adobe Photoshop\Adobe Photoshop 2021\Photoshop.exe"
            osfunc(PSpath)

        elif 'shutdown' in query or 'stop' in query:  # code for stopping the loop or shutting down jenny
            speak("Going to sleep now. Goodbye!")
            exit()

