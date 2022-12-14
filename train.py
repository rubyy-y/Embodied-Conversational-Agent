import os
import json
import numpy as np
from preprocessing import preprocess, bag_of_words

try:
    os.chdir("Embodied-Conversational-Agent")
except:
    pass

with open('intents.json', 'r') as f:
    intents = json.load(f)

all_words, tags, xy = [], [], []
for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)

    for pattern in intent['patterns']:
        word = preprocess(pattern)
        all_words.extend(word) # extend because all words is array
        xy.append((word, tag))

# make set to remove duplicates, but return as list via sorted
all_words = sorted(set(all_words))

# TODO - add intents
tags = sorted(set(tags))

X_train, y_train = [], []
for (pat, tag) in xy:
    bow = bag_of_words(pat, all_words)
    X_train.append(bow)

    # numbers for labels
    label = tags.index(tag) 
    y_train.append(label) # for cross entropy loss (not 1-hot)

X_train = np.array(X_train)
y_train = np.array(y_train)

# Pytorch Dataset - makes iteration and batch training easier
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader


class ChatDataSet(Dataset):
    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train

    def __getitem__(self, index):
        return (self.x_data[index], self.y_data[index])

    def __len__(self):
        return self.n_samples

# Hyperparameters
batch_size = 8
num_workers = 0
lr = 0.001
num_epochs = 1000
    
dataset = ChatDataSet()
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=num_workers)

# Model
from model import NertalNetwork

input_size = len(X_train[0])
hidden_size = 8
output_size = len(tags) # is number of classes

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = NertalNetwork(input_size, hidden_size, output_size)

# Error and Optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=lr)

# Training Loop
for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)

        # forward pass
        outputs = model(words)
        loss = criterion(outputs, labels)

        # backward an optimizer step
        optimizer.zero_grad() # empty gradients
        loss.backward()
        optimizer.step()

    # every 100 epochs
    if (epoch+1) % 100 == 0:
        print(f'epoch {epoch+1}/{num_epochs}, loss = {loss.item():.4f}')

print(f'Final Loss: {loss.item():.4f}')

# Save Model
data = {
    "model_state": model.state_dict(),
    "input_size": input_size,
    "hidden_size": hidden_size,
    "output_size": output_size,
    "all_words": all_words,
    "tags": tags
}

file = "model_data.pth"
torch.save(data, file)

print(f'Training is complete. Data saved to {file}.:)')