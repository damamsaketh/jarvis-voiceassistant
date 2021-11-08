import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

engine=pyttsx3.init()
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)
listener=sr.Recognizer()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening to you . . .")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'jarvis' in command:
                command=command.replace('jarvis','')




    except:
        pass
    return command


def run_jarvis():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('time is'+time)
    elif 'tell me about' in command:
        person=command.replace('tell me about','')
        data=wikipedia.summary(person,1)
        print(data)
        talk(data)
    elif 'bye' in command:
        talk('Bye saketh,have a nice day')
        print('Bye saketh,have a nice day')
    elif 'message' in command:
        talk("enter the phone number you want the msg sent to")
        phnno = str(input("enter the phone no you want the msg sent to"))
        talk(phnno)
        talk("enter the message")
        msg = str(input("enter the message"))
        talk(msg)
        talk("enter when you want to send 'hour'")
        hour = int(input("enter when you want to send 'hour'"))
        talk(hour)
        talk("what about minutes")
        min = int(input("minutes?"))
        talk(min)
        pywhatkit.sendwhatmsg(phnno, msg, hour, min)
    elif 'how are you' in command:
        talk("I'm splendid!Thank you for asking")
        print("I'm splendid!Thank you for asking")


    else:
        talk("repeat the question")


while True:
    run_jarvis()

