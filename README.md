# VoiceGPT 

This is a voice-based AI chatbot that uses Google Speech Recognition, OpenAI GPT-3 API, and Eleven Labs API to transcribe user's voice input, generate an AI-generated response, convert the response to speech, and play it back to the user.

## Features

- Transcribes user's voice input to text using Google Speech Recognition API.
- Generates AI-generated responses using OpenAI GPT-3 API.
- Converts text responses to speech using Eleven Labs API.
- Plays the generated audio response back to the user.
- Handles errors gracefully and displays appropriate error messages.

## Prerequisites

In order to use this chatbot, you will need the following:

- Python 3.x installed on your machine.
- API keys for Google Speech Recognition, OpenAI GPT-3, and Eleven Labs. Instructions for obtaining these keys can be found in the respective API documentation.
- The following Python libraries installed:
  - `io`
  - `os.path`
  - `time`
  - `pyaudio`
  - `pydub`
  - `pydub.playback`
  - `speech_recognition`
  - `elevenlabslib` (custom library for Eleven Labs API)
  - `openai`
  - `playsound`

## Setup

1. Clone the repository to your local machine.
2. Install the required Python libraries mentioned in the prerequisites section.
3. Obtain the API keys for Google Speech Recognition, OpenAI GPT-3, and Eleven Labs, and replace the placeholder API keys in your Python script (e.g., "VoiceGPT.py") with your actual API keys.
4. Run your Python script (e.g., "VoiceGPT.py") using Python 3.x to start the chatbot.

## How to Use

1. Start the chatbot by running your Python script (e.g., "VoiceGPT.py") using Python 3.x.
2. Say "desired command that you choose" to trigger the chatbot and start recording your question.
3. After recording your question, the chatbot will transcribe your voice input to text and generate an AI-generated response.
4. The response will be converted to speech and played back to you.
5. You can ask multiple questions by repeating the process.
6. The chatbot will continue running until you manually stop it.

## Troubleshooting

- If the chatbot is not transcribing voice input correctly, make sure you have a good quality microphone and there is no background noise.
- If there are issues with the API keys, make sure you have entered the correct keys in your Python script (e.g., "VoiceGPT.py").
- If there are any errors during the execution of the program, check the error messages displayed and refer to the API documentation for troubleshooting.

##
Sometimes you will need to restart the chatbot for it to work properly. this is a known bug and i am working on it.

## Credits

This chatbot uses the following APIs and libraries:

- Google Speech Recognition API: https://pypi.org/project/SpeechRecognition/
- OpenAI GPT-3 API: https://beta.openai.com/docs/
- Eleven Labs API: Custom library provided by Eleven Labs (https://eleven-labs.com/)
- PyAudio: https://people.csail.mit.edu/hubert/pyaudio/docs/
- PyDub: https://pydub.com/
- Playsound: https://pypi.org/project/playsound/

## License

This chatbot is released under the [LICENSE](LICENSE) file. Please review the terms and conditions before using or modifying this software.

https://user-images.githubusercontent.com/87999692/232620534-dda72918-8632-4bf9-bd04-565551134ddf.mp4

