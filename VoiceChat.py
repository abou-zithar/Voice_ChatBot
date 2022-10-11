from typing import Mapping
from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys
import nltk
nltk.download('omw-1.4')

recongizer= speech_recognition.Recognizer()

speaker= tts.init()
speaker.setProperty('rate', 150)

todo_list=['Go shopping','Clean Room','Record Video']

def create_note():
    global recongizer

    speaker.say('What do you want to write onto your note?')

    speaker.runAndWait()

    done=False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recongizer.adjust_for_ambient_noise(mic,duration=0.2)
                
                audio = recongizer.listen(mic)
                note=recongizer.recognize_google(audio)
                note=note.lower()

                speaker.say('Choose a file name')
                speaker.runAndWait()
                recongizer.adjust_for_ambient_noise(mic,duration=0.2)
                
                audio = recongizer.listen(mic)
                filename=recongizer.recognize_google(audio)
                filename=filename.lower()
            with open(f"{filename}.txt",'w') as f:
                f.write(note)
                done=True
                speaker.say(f'I successfully created the note{filename}')
                speaker.runAndWait()   
        except speech_recognition.UnknownValueError:
            recongizer=speech_recognition.Recognizer()
            speaker.say('I did not understand you! Please try again')
            speaker.runAndWait()

    


def add_todo():
    global recongizer

    speaker.say('What do you want to add?')

    speaker.runAndWait()
    done=False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recongizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio=recongizer.listen(mic)
                item=recongizer.recognize_google(audio)
                item=item.lower()
                todo_list.append(item)

                done=True

                speaker.say(f'I added {item} to the to do list')
                speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recongizer=speech_recognition.Recognizer()
            speaker.say('I did not understand you! Please try again')
            speaker.runAndWait()
def hello():
    speaker.say('Hello,What Can i do for you?')
    speaker.runAndWait()

def quit():
    speaker.say('Bye')
    speaker.runAndWait()
    sys.exit(0)


def show_todo():
    speaker.say('The items in your to do list are the following')
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()



Mapping={
    'greeting':hello,
    'create_note':create_note,
    'add_todo':add_todo,
    'show_todos':show_todo,
    'exit':quit
}
assistant= GenericAssistant('intents.json',intent_methods=Mapping)

assistant.train_model()
assistant.save_model()
assistant.load_model()


while True:
    try:
        with speech_recognition.Microphone() as mic:
            recongizer.adjust_for_ambient_noise(mic,duration=0.2)
            audio=recongizer.listen(mic)

            massage=recongizer.recognize_google(audio)
            massage=massage.lower()

        assistant.request(massage)
    except speech_recognition.UnknownValueError:
            recongizer=speech_recognition.Recognizer()
           
           