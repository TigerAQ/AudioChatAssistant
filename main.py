# setup env
import os
from API import OpenAI_API_Key
import subprocess
import objc
from langchain.llms import OpenAI
model_engine = "gpt-4"  # Use the GPT-4 model
import speech_recognition as sr
import pyttsx3

# Initialize the audio recognizer
r = sr.Recognizer()

# create function to record audio
def record_text():
    while True:
        try:
            with sr.Microphone() as source2:  # use the micro as source for input
                r.adjust_for_ambient_noise(source2, duration=0.2)  # prep recognizer to receive input
                print("I'm listening, how can I help?")
                audio2 = r.listen(source2)  # listens for user input
                test = r.recognize_google(audio2)  # using google to recognize audio
                return test
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")

# create function to speak text
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# create the main function
def main():
    # Initialize conversation history
    messages = [
        {"role": "system", "content": "You are a helpful and humorous assistant, you will help the user to gain information and answer their questions whiling making proper jokes."}
    ]

    while True:
        input_text = record_text()
        if input_text:
            print(f"User: {input_text}\n")
            messages.append({"role": "user", "content": input_text})

            # Send message to GPT-4 and get response
            response = openai.ChatCompletion.create(
                model=model_engine,
                messages=messages,
            )
            response_text = response.choices[0].message.content

            # Add AI's response to chat history
            messages.append({"role": "assistant", "content": response_text})

            print(f"GPT-4: {response_text}\n")
            speak(response_text)


def speak(text:str):
    subprocess.call(['say', text])

if __name__ == "__main__":
    main()
