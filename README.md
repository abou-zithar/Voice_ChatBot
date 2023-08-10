# Voice-Controlled Personal Assistant

This is a Python script that implements a voice-controlled personal assistant using the `neuralintents` library. The assistant can perform tasks like creating notes, adding to-do list items, displaying the to-do list, and more, all through voice commands.

## Prerequisites

Before running the script, you need to have the following libraries installed:

- `neuralintents`: Install using `pip install neuralintents`
- `speech_recognition`: Install using `pip install SpeechRecognition`
- `pyttsx3`: Install using `pip install pyttsx3`
- `nltk`: Install using `pip install nltk`

Additionally, download the "omw-1.4" data from NLTK by running the following command:

```bash
nltk.download('omw-1.4')
```

## Features
1. ### Create Notes:
 You can create text notes by speaking your desired content and providing a filename. The assistant will save the content as a text file.

2. ### Add To-Do List Items:
    You can add items to your to-do list by speaking the task's description. The assistant will add the task to the list and confirm the addition.

3. ### Display To-Do List:
    The assistant can read out the current to-do list items to you.

4. ### Greeting and Exit:
   The assistant greets you when you start and can be exited by voice command.
## How to Use
1.  Run the script in your Python environment.

2.  The assistant will greet you. You can interact with it using voice commands.

3.  For creating a note, speak the content you want to write and provide a filename when prompted.

4.  To add a to-do list item, speak the task description when prompted.

5.  Ask the assistant to display your to-do list by using the appropriate command.

6.  You can exit the assistant by using the exit command.

## Configuration
- The assistant uses the intents.json file to understand user commands and map them to functions.

- The Mapping dictionary defines the intent-method mappings for the assistant.

## Important Notes
- The assistant utilizes the Google Web Speech API for speech recognition. If you encounter issues with recognition, you may need an active internet connection and ensure your microphone is properly configured.

- If the assistant does not understand your command, it will ask you to repeat the command.

- The assistant continues to run in a loop until you exit the script.

- The assistant's functionality can be extended by modifying the Mapping dictionary and adding corresponding methods.

## Acknowledgments
This project uses the neuralintents library, which simplifies the process of creating a neural network-based chatbot. It also uses various speech-related libraries to enable voice-based interactions.

## Author
Created by [Mahmoud abou Zithar]

## License
This project is licensed under the MIT License.
