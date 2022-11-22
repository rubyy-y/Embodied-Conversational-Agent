# Embodied-Conversational-Agent
Project in the scope of the Artificial Intelligence Bachelor study at JKU Linz.

This Project aims at programming an Embodied Conversational Agent for Game Analysis. <br>
As a programming language, it will use primarily Python, but I might consider using HTML and CSS in the process.

Progress updates on this project will be presented roughly every three weeks on the JKU campus.

## Chatbot Files
* intents.json - pure data file; controls text responses
* preprocessing.py - preprocess function to convert string into usable tokens
* model.py - pytorch model; Neural Network
* train.py - training loop for model.py
* chat.py - loads model and gives response

## App Files
* app.py - Flask App
* app.js - JavaScript for app
* base.html - base template
* style.css - styling

## Important Package Versions
* python 3.10.4
* numpy 1.22.3
* pandas 1.4.2
* nltk 3.7
* torch 1.11.0
* flask 2.1.3


### To-Do
add more intents <br>
-> how are you - extra <br>
-> what can you do? <br>
-> what is your name, about you <br>
create data visualizations <br>
implement data visualizations on website <br>