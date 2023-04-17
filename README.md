# VoiceGPT
VoiceGPT uses Google Speech Recognition,  GPT-3, and Eleven Labs.
This program is a voice-based AI chatbot that uses Google Speech Recognition, OpenAI GPT-3 API, and Eleven Labs API to transcribe user's voice input, generate an AI-generated response, convert the response to speech, and play it back to the user.

The program starts by initializing the necessary APIs and setting up the required credentials. It defines functions for transcribing audio to text using Google Speech Recognition API, generating AI-generated audio bytes using Eleven Labs API, playing audio files, and generating a response using OpenAI GPT-3 API.

The main part of the program is the main() function, which runs an infinite loop and listens for the user to say "siri" to start recording their question. Once the user says "siri", the program records the user's voice input, transcribes it to text, generates a response using GPT-3 API, converts the response to speech using Eleven Labs API, plays the generated audio to the user, and then deletes the temporary audio files.

If any errors occur during the process, such as failure in transcribing audio or playing audio, appropriate error messages are displayed.






https://user-images.githubusercontent.com/87999692/232620534-dda72918-8632-4bf9-bd04-565551134ddf.mp4

