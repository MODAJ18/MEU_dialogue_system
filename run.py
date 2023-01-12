from src.NLU.intention import IntentRecognizer
from src.dialog_manager.manage import verify_intent
from src.dialog_manager.manage import manage_dialog

import pickle
import os
import random
import datetime
import torch
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
from parrot import Parrot
from transformers import pipeline, Conversation

import warnings
warnings.filterwarnings("ignore")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
            print(f"User said: {query}\n")  #User query will be printed.
        except Exception as e:
            # print(e)  use only if you want to print the error!
            print("Say that again please...")   #Say that again will be printed in case of improper voice
            return "None" #None string will be returned
        return query

def get_discourse(query_in, labels_in):
    zsc_result = zs_model(query_in, labels_in)
    zsc_labels = zsc_result["labels"]
    zsc_scores = zsc_result["scores"]
    discourse_prediction = zsc_labels[zsc_scores.index(max(zsc_scores))]
    return discourse_prediction

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet_time():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

initial_states = {"music": {"none": "off"},
                  "lights": {"none": "on", "bedroom": "on", "washroom":"on", "kitchen": "on"},
                  "volume": {"none":"3"},
                  "heat": {"none":"warm", "bedroom":"warm", "washroom":"warm", "kitchen": "warm"},
                  "lamp": {"none": "off"},
                  "newspaper": {"none": "not brought"},
                  "juice": {"none": "not brought"},
                  "socks": {"none": "not brought"},
                  "chinese": {"none": "off"},
                  "korean": {"none": "off"},
                  "english": {"none": "on"},
                  "german": {"none": "off"},
                  "shoes": {"none": "not brought"}}


if __name__ == "__main__":
    with open('Saved/intention_models.pickle', 'rb') as handle:
        intention_models_trained_b = pickle.load(handle)
    with open('Saved/tfidfV.pickle', 'rb') as handle:
        tfidfv_b = pickle.load(handle)
    with open('Saved/les.pickle', 'rb') as handle:
        les_b = pickle.load(handle)

    ir_b = IntentRecognizer()
    ir_b.intent_models = intention_models_trained_b

    zs_model = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    converser = pipeline("conversational", model="facebook/blenderbot-400M-distill")

    states = initial_states

    # setting up the voice
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')  # gets you the details of the current voice

    engine.setProperty('voice', voices[1].id)  # 0-male voice , 1-female voice
    engine.setProperty('rate', 200)

    discourse_labels = ["conversational", "command"]

    greet_time()
    prev_response = ""

    while True:
        query = takeCommand().lower()  # Converting user query into lower case
        print("QUERY: {}".format(query))
        discourse_prediction = get_discourse(query_in=query, labels_in=discourse_labels)
        print(discourse_prediction)

        if query == "none" or len(query) == 0:
            continue

        if discourse_prediction == "command":
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                if query == "":
                    query = "nothing"
                results = wikipedia.summary(query, sentences=5)
                print(results)
                response = "According to Wikipedia, {}".format(results)
                speak(response)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
                response = "youtube opened"
                speak(response)

            elif 'open google' in query:
                webbrowser.open("google.com")
                response = "google opened"
                speak(response)

            elif 'play music' in query:
                music_dir = 'music_dir_of_the_user'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
                response = "playing music"

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                response = f"Sir, the time is {strTime}"
                speak(response)

            elif ('open stackoverflow' in query) or ('open stack overflow' in query):
                webbrowser.open('stackoverflow.com')
                response = "stackoverflow opened"

            elif ('open free code camp' in query) or ('open freecodecamp' in query):
                webbrowser.open('freecodecamp.org')
                response = "freecodecamp opened"

            else:
                if "in home" in query:
                    intents = ir_b.get_intents(query, les_b, tfidfv_b)
                    if intents['object'] == "none":
                        intents['object'] = "english"
                        print(intents)

                    # manage dialog and state change
                    ver_intent = intents
                    states_main, prompt_main, prev_states_main = manage_dialog(ver_intent, states)
                    if len(prompt_main) == 1:
                        response = prompt_main[0]
                    #                     print(ver_intent["object"], prev_states_main[ver_intent["object"]])
                    #                     print(ver_intent["object"], states_main[ver_intent["object"]])
                    else:
                        response = " ".join(prompt_main[:-1])
                    speak(response)
                else:
                    # asking
                    conversation = Conversation(query)
                    response = converser(conversation).generated_responses[-1]
                    speak(response)


        elif discourse_prediction == "conversational":
            conversation = Conversation(query)
            # responses = converser(conversation).generated_responses
            # response_ind = random.randint(0, len(responses))
            # response = responses[response_ind]
            response = converser(conversation).generated_responses[-1]
            speak(response)

        prev_response = response

