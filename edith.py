import psutil
import pylint
import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
import wolframalpha
import subprocess
import time
import json
import operator
import requests
import pyjokes
from PIL import Image , ImageGrab 
from twilio.rest import Client

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[0].id)

def takeCommand():
       #It takes voice input from user using a mic and returns string output
       r=sr.Recognizer()
       with sr.Microphone() as source:
              print("Listening....")
              r.pause_threshold=1
              audio = r.listen(source)

       try:

              print("Recognizing...")
              query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
              print(f"User said: {query}\n")  #User query will be printed.
    
       except Exception as e:  #exception
              print(e)
              print("Could you please repeat that...")   #"Could you please repeat that..." will be printed in case of improper voice input
              return "None" #None string will be returned
       return query                

def speak(audio):
       engine.say(audio)
       engine.runAndWait() #Without this command, speech will not be audible to us.

#wishing the user when the program starts to run 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    #good morning, good afternoon or good evening messages , depending upon the time of day at which the program runs
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")   

    else:
        speak("Good Evening Sir!")  

    speak("I am EDITH . How may I help you ?")  

def getmemory() :
       pid = os.getpid()
       py = psutil.Process(pid)
       return py.memory_info()[0] / 2. ** 30

def takeScreenshot():
       image=ImageGrab.grab()
       image.show()

def sendEmail(to, content):
       server = smtplib.SMTP('smtp.gmail.com', 587)
       server.ehlo()
       server.starttls()
       server.login('youremailid@gmail.com', 'yourpassword')  #you need to provide your email id and password for it to run without any errors
       server.sendmail('youremailid@gmail.com', to, content)
       server.close() 

#driver code
if __name__=="__main__" :
       speak("Even Dead, I'm The Hero")  #E.D.I.T.H
       wishMe() #calls the wishing function 
       while True:
              query = takeCommand().lower() #Converting user query into lower case
              
              if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
                     speak('Searching Wikipedia...')
                     query = query.replace("wikipedia", "")
                     results = wikipedia.summary(query, sentences=2)  #we have limited the no. of sentences returned to 2. That may be changed as per the user's preference
                     speak("According to Wikipedia")
                     print(results)  #text output of the wikipedia findings
                     speak(results)   #speech output of the wikipedia findings

              elif 'hello' in query:  
                     speak("Hello sir")

              elif 'who are you' in query:
                     speak("I'm Edith , Mr.Anirban Raha's personal desktop assistant")

              elif 'how are you' in query:
                     speak("I'm doing great")

              elif 'joke' in query:   #returns a joke using pyjokes module
                     speak(pyjokes.get_joke())

              elif 'full form' in query or 'what does your name mean' in query:
                     speak("EDITH stands for Even Dead, I'm the hero. It is an homage to Tony Stark's augmented intelligence technology")

              elif 'open twitter' in query: #opens twitter
                     webbrowser.open("twitter.com")

              elif 'open amazon' in query:  #opens amazon
                     webbrowser.open("amazon.com")

              elif 'open netflix' in query:      #opens netflix
                     webbrowser.open("netflix.com")

              elif 'open notepad' in query:  #opens notepad on windows pc
                     os.system('notepad')

              elif 'open imdb' in query:   #opens imdb
                     webbrowser.open("imdb.com")

              elif 'open instagram' in query:           #opens instagram
                     webbrowser.open("instagram.com")

              elif 'open pinterest' in query:      #opens pinterest
                     webbrowser.open("pinterest.com")

              elif 'open linkedin' in query: #opens linkedin
                     webbrowser.open("linkedin.com")

              elif 'open coursera' in query:     #opens coursera 
                     webbrowser.open("coursera.com")

              elif 'open quora' in query:     #opens quora
                     webbrowser.open("quora.com")

              elif 'open github' in query:      #opens github
                     webbrowser.open("github.com")

              elif 'open reddit' in query:        #opens reddit
                     webbrowser.open("reddit.com")

              elif 'open flipkart' in query:        #opens flipkart
                     webbrowser.open("flipkart.com")

              elif 'take screenshot' in query:
                     time.sleep(1)
                     takeScreenshot()
              
              elif 'youtube' in query:     #if youtube is present in query input
                     if 'open' in query:       #if query is to open youtube
                            webbrowser.open("https://youtube.com")
                     else:                 #if query is to search something on youtube
                            query = query.replace("youtube", "")
                            query = query.replace("search", "")
                            query = query.replace(" ", "+")
                            print("search: ", query)
                            webbrowser.open("https://www.youtube.com/results?search_query="+query)

              elif 'google' in query:       #if qoogle is present in query input
                     if 'open' in query:      #if query is to open google
                            webbrowser.open("https://google.com")
                     else:                #if query is to search something on google
                            query = query.replace("google", "")
                            query = query.replace("search", "")
                            query = query.replace(" ", "+")
                            webbrowser.open("https://google.com/search?q="+query)

              elif 'open stackoverflow' in query:      #opens stackoverflow
                     webbrowser.open("stackoverflow.com")

              elif 'open facebook' in query:        #opens facebook
                     webbrowser.open("facebook.com")   

              elif "write a note" in query:    #function to write a note in notepad
                     speak("What should i write, sir")
                     note = takeCommand()       #takes input for body of note
                     file = open('edith.txt', 'w') 
                     file.write(note)      
                    
              elif "display note" in query:    #display the written note
                     file = open("edith.txt", "r")
                     print(file.read())
                     speak(file.read(6))

              elif "get memory" in query:
                     print(getmemory())

              elif 'the time' in query:       #time of the day in hrs , mins , secs
                     strTime = datetime.datetime.now().strftime("%H:%M:%S") 
                     print(f"Sir, the time is {strTime}")
                     speak(f"Sir, the time is {strTime}")

              elif 'open microsoft word' in query:
                     speak("Opening Microsoft Word")
                     os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007.lnk")

              elif 'open microsoft powerpoint' in query:
                     speak("Opening Microsoft Powerpoint")
                     os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office PowerPoint 2007.lnk")

              elif 'open microsoft excel' in query:
                     speak('Opening Microsoft Excel')
                     os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007.lnk")

              elif 'open microsoft outlook' in query:
                     speak('Opening Microsoft Outlook')
                     os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Outlook 2007.lnk")

              elif 'open paint' in query:
                     speak("Opening paint")
                     os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint.lnk")

              elif "calculate" in query:    #calculates math equations using wolfram alpha api
                     app_id = "L6XT8Q-QL4X9G67LX"           #create an account on wolframalpha for user specific app_id
                     client = wolframalpha.Client(app_id)
                     indx = query.lower().split().index('calculate')
                     query = query.split()[indx + 1:]
                     res = client.query(' '.join(query)) 
                     answer = next(res.results).text
                     print("The answer is " + answer)      
                     speak("The answer is " + answer)

              elif "question" in query:  #answers questions using wolfram alpha api
                     app_id="L6XT8Q-QL4X9G67LX"             #create an account on wolframalpha to give user specific app_id
                     client = wolframalpha.Client(app_id)
                     indx = query.lower().split().index('question')
                     query = query.split()[indx + 1:]
                     res = client.query(' '.join(query))
                     answer = next(res.results).text 
                     print(answer)
                     speak(answer)

              elif 'play music' in query:         #music played from a playlist 
                     music_dir = 'F:\\music'     #must provide the folder location where playlist is located 
                     songs = os.listdir(music_dir)
                     print(songs)
                     os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs)-1)]))       #random module used for shuffle function in playlist

              elif 'date' in query:      #current date returned
                     cmd='date'
                     os.system(cmd)

              elif 'c drive' in query:        #opens the machine's C drive
                     os.system('explorer C:\\"{}"'.format(query.replace('c drive','')))

              elif 'email to recipient' in query:        #email to a predecided gmail user
                     try:
                            speak("What should I say?")
                            content = takeCommand()         #takes command for body of the email
                            to = "youremailid@gmail.com"    #your less secure app access must be turned on
                            sendEmail(to, content)
                            speak("Email has been sent!")
                     except Exception as e:
                            print(e)
                            speak("Sorry sir . I was not able to send the email")      #error while trying to send the email

              elif 'open code' in query:
                     codePath = "E:\\Microsoft VS Code\\Code.exe"     #this might vary depending on the user's machine
                     os.startfile(codePath)

              elif "restart" in query:          #restarts your windows pc
                     subprocess.call(["shutdown", "/r"])

              elif 'shutdown system' in query:      #shuts down your windows pc
                     speak("Hold On a Second ! Your system is on its way to shut down")
                     subprocess.call(["shutdown", "/s", "/t", "60"])          #it will shut down after 60sec

              elif "where is" in query:       #if the query is to find the location of a place 
                     query = query.replace("where is", "")
                     location = query
                     speak("User asked to Locate")
                     speak(location)
                     webbrowser.open("https://www.google.nl/maps/place/" + location + "")

              elif 'awesome' in query or 'wow' in query or 'amazing' in query or 'wonderful' in query:
                     speak("Thank you sir")

              elif 'edith quit' in query or 'exit' in query or 'close' in query or 'abort' in query:  #quitting the program
                     speak("Have a good day sir")
                     exit()

              
       

              
       
       
           

       
       

 
              
             
       



       




       
           

       
       

 
              
             
       



       



