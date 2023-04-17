import io
import os.path
import time
import pyaudio
import pydub
import pydub.playback
import speech_recognition as sr
from elevenlabslib import ElevenLabsUser
import openai
from playsound import playsound


# Initialize APIs
openai.api_key = "Your API Key"
elevenlabs_api_key = "Your API Key"
user = ElevenLabsUser(elevenlabs_api_key)
voice_name = "Your Voice Name"

def transcribe_audio_to_text(filename):
    """Transcribes audio file to text using Google Speech Recognition API."""
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source) 
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

def generate_audio_bytes(prompt):
    """Generates AI-generated audio bytes using Eleven Labs API."""
    voice = user.get_voices_by_name(voice_name)[0]
    audio_bytes = voice.generate_audio_bytes(prompt)
    with open('output.mp3', 'wb') as f:
        f.write(audio_bytes)
    return 'output.mp3'


def play(filename):
    while not os.path.exists(filename):
        time.sleep(0.1)
    try:
        playsound(filename)
    except Exception as e:
        print(f"Could not play audio: {e}")

def generate_response(prompt):
    """Generates a response using OpenAI GPT-3 API."""
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"]

def main():
    """Listens for user input and generates an AI-generated response and audio."""
    recognizer = sr.Recognizer()
    while True:
        # Wait for user to say "Computer"
        print("Say 'name of bot' to start recording your question")
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
        try:
            transcription = recognizer.recognize_google(audio)
            if transcription.lower() == "your name of bot":
                # Record audio
                filename = "input.wav"
                print("Say your question")
                with sr.Microphone() as source:
                    source.pause_threshold = 0
                    audio = recognizer.listen(source)
                    with open(filename, "wb") as f:
                        f.write(audio.get_wav_data())
                        

                # Transcribe audio to text 
                text = transcribe_audio_to_text(filename)
                if text:
                    print(f"You said: {text}")

                    # Generate the response
                    response = generate_response(text)
                    print(f"Chat GPT-3 says: {response}")

                    # Generate AI-generated audio and play it
                    audio_filename = generate_audio_bytes(response)
                    playsound(audio_filename)
                                        # Delete files

                    os.remove(audio_filename)
                    os.remove(filename)
        except sr.UnknownValueError:

            
           
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()