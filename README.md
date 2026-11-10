Language Translator
A sleek, modern desktop application built with Python for instant text translation across multiple languages.

Description
The Language Translator application provides a simple, dark-themed graphical user interface (GUI) to translate text seamlessly between supported languages. Built using customtkinter for a clean visual experience and deep_translator to interface with translation services, the application allows users to select source and target languages (including English, German, French, Spanish, Hindi, Malayalam, Tamil, Telugu, and Kannada), enter custom text, and receive real-time translations. Designed for the Stardance Challenge, this utility aims to break communication barriers with an intuitive desktop experience.

Getting Started
Dependencies
Operating System: Windows 10/11, macOS, or Linux
Python Version: Python 3.8 or higher
Python Packages:
customtkinter
deep-translator

Installing
Clone or Download the Project:
Download or clone the repository to your local directory. Ensure app.py is present.

Set Up a Virtual Environment (Optional but Recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Prerequisites:
Run the following command to install the required dependencies:
pip install customtkinter deep-translator

Executing Program
Follow these steps to run the application:
Open your terminal or command prompt.
Navigate to the project directory containing app.py.
Launch the application:
python app.py
Type your text into the top input text box.
Choose your source language under From Language and target language under To Language.
Click the Translate button to view the result in the output box below.
Use Clear All to reset the input/output fields or About App for version information.

Help
Translation Errors: Verify that your internet connection is active, as the application requires network access to query the translation API.
Missing Module Errors: If you see a ModuleNotFoundError, make sure you have installed all required packages in your active Python environment:
pip install -r requirements.txt
App Information: Click the About App button within the UI to view project details.

License

This project is licensed under the MIT License - see the LICENSE.md file for details.

<img width="1917" height="1077" alt="readme" src="https://github.com/user-attachments/assets/3b2f02a3-a1d8-4ee3-b067-f88fb8bccb46" />
