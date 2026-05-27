Python Text-to-Speech Application using pyttsx3

This project is a simple Text-to-Speech (TTS) application built with Python and the pyttsx3 library.
The program allows users to convert custom text into spoken audio while giving control over voice selection and speech speed.

Features
Convert text into speech
Adjustable speech speed
Multiple voice selection
Displays all available system voices
Offline speech synthesis (no internet required)
Beginner-friendly Python project
How It Works

The application uses the pyttsx3 library to initialize a speech engine and retrieve all available voices installed on the operating system. The user can:

Choose the speech speed
Select a voice from the available options
Enter custom text
Hear the generated speech output

The program then processes the text and plays it aloud using the selected voice configuration.

Technologies Used
Python
pyttsx3
Requirements

Install the required library:

pip install pyttsx3
Example Usage
speak("Hello world", 150, 0)
Project Purpose

This project was created to practice:

Python functions
User input handling
Text-to-speech systems
Working with external Python libraries
