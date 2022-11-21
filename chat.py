import os
import random
import json
import torch
from model import NertalNetwork
from preprocessing import preprocess, bag_of_words

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

os.chdir("Embodied-Conversational-Agent")
with open('intents.json', 'r') as f:
    intents = json.load(f)

file = "model_data.pth"
data = torch.load(file)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NertalNetwork(input_size, hidden_size, output_size)
model.load_state_dict(model_state)
model.eval()

# Create Chat
bot_name = "Bot ohne Name"
print("Chat is now open. Type 'exit' to exit.")

while True:
    sentence = input('You: ')
    if sentence == "exit":
        break

    sentence = preprocess(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    # TODO - if unsure ... softmax
    probabilities = torch.softmax(output, dim=1)
    probability = probabilities[0][predicted.item()]
    
    if probability > 0.8:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                print(f"{bot_name}: {random.choice(intent['responses'])}")
    
    else:
        print(f"{bot_name}: I'm sorry, I do not understand that yet. Could you reformulate your request?")
