from logging import exception
from gtts import gTTS
import pyttsx3
import PyPDF2
import os
import pyttsx3
import speech_recognition as sr
import google

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    engine.say(audio)
    engine.runAndWait()


def voice_command():

    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as s:
        
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(s)
        audio = r.listen(s)
        speak("Enter drive name, like C, or D, or E, or F :")
    
    try:

        print("Listening...")

        query = r.recognize_google(audio, language='en') 
        print("Recognizing...") 
        speak(query)
        print(f"User said: {query}\n")

        dr_up = query
        
        if dr_up == 'C' or dr_up=='c':
              
              usr = input("\nOS users name as given :")
              loc = input("\nEnter file location [Desktop / Download] :")
              fi =  input("\nTxt file name as given :")

              p = open(dr_up+":/Users/"+usr+"/"+loc+"/"+fi+".txt","r")
              mtest = p.read().replace("\n", " ")
              language = 'en'
              op = gTTS(text=mtest, lang=language, slow=False)
              op.save("op.mp3")
              print("Playing......")
              os.system("start op.mp3")
        
        elif dr_up=='D' or dr_up=='E' or dr_up=='F' or dr_up=='G':
            
             
             loc = input("\nFolder name as given :")
             fi =  input("\nTxt file name as given :")
             p = open(dr_up+":/"+loc+"/"+fi+".txt","r")
             mtest = p.read().replace("\n", " ")
             language = 'en'
             op = gTTS(text=mtest, lang=language, slow=False)
             op.save("op.mp3")
             print("Playing......")
             os.system("start op.mp3")
        else:
            print("\nGiven input is wrong")
            return voice_command()
    
    except Exception:
        return"None"


    return voice_command()



def serch():
    

    try:
        dr = input("\n\nEnter drive name [C/D/E/F] :")
        dr_up = dr.upper()
        
        if dr == 'C' or dr=='c':
              
              usr = input("\nOS users name as given :")
              loc = input("\nEnter file location [Desktop / Download] :")
              fi =  input("\nTxt file name as given :")

              p = open(dr_up+":/Users/"+usr+"/"+loc+"/"+fi+".txt","r")
              mtest = p.read().replace("\n", " ")
              language = 'en'
              op = gTTS(text=mtest, lang=language, slow=False)
              op.save("op.mp3")
              print("Playing......")
              os.system("start op.mp3")
        
        elif dr_up=='D' or dr_up=='E' or dr_up=='F' or dr_up=='G':
             
             
             loc = input("\nFolder name as given :")
             fi =  input("\nTxt file name as given :")
             p = open(dr_up+":/"+loc+"/"+fi+".txt","r")
             mtest = p.read().replace("\n", " ")
             language = 'en'
             op = gTTS(text=mtest, lang=language, slow=False)
             op.save("op.mp3")
             print("Playing......")
             os.system("start op.mp3")

        else:
            print("\nGiven input is wrong")
            return serch()

    
    except(ValueError,SyntaxError,TypeError,IndexError,FileNotFoundError):
        print("\nGiven input is wrong")
        return serch()

    

def manual():
    p = int(input("\n\nFor C drive [press-1]\nFor others drive [press-2] :"))

    if p==1:
       str = "C:\\Users\\Fahim\\Desktop\\document_name.txt"
       
       print("\nEnter Location for C drive file like:\n"+str)

       get = input("\n")
       file = open(get,"r")
       test = file.read().replace("\n", " ")
       language = 'en'
       op = gTTS(text=test, lang=language, slow=False)
       op.save("op.mp3")
       print("Playing......")
       os.system("start op.mp3")
    
    else:
       str = "[D/E/F/G]:\\Folder_name\\document_name.txt"
       
       print("\n\nEnter Location for others drive like:\n"+str)

       get = input("\n")
       file = open(get,"r")
       test = file.read().replace("\n", " ")
       language = 'en'
       op = gTTS(text=test, lang=language, slow=False)
       op.save("op.mp3")
       print("Playing......")
       os.system("start op.mp3")
       

def create():
      p = input("Enter [txt] File name: ")
      speak("\nYou Named the file name as : "+p)
      

      p1 = open(p+".txt", "w")

      p2 =input("Enter your text:\n")
      

      p1.write(p2)
      p1.close()

      readd=open(p+".txt","r")

      test = readd.read().replace("\n", " ")
      language = 'en'
      op = gTTS(text=test, lang=language, slow=False)
      op.save("op.mp3")
      print("Playing......")
      os.system("start op.mp3")
      
      
      

      readd.close()

def re_used():
    
    engine.runAndWait(50)
    speak("\nFor again use the service [Press-1].\nFor exit[press-2] :")
    p = int(input("\nFor again use the service [Press-1].\nFor exit[press-2] :"))
    
    
    

    if p==1:
        main()
    else:
        return 0

def new_func():
    
    book = open('p.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages

    speaker = pyttsx3.init()
    for num in range(7, pages):
        page = pdfReader.getPage(num)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()
    return 10


def main():
  n = int(input("What you need\nFor search [press-1] and\nFor manual input [press-2]\nFor make text [press-3] : "))

  if n==1:
     new_func()
     re_used()

  elif n==2:
     manual()
     re_used()

  elif n==3:
     create()
     re_used()
  else:
      voice_command()




main()

        
        

             




