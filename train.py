import os
import json
import numpy as np
from preprocessing import preprocess, bag_of_words

os.chdir("Embodied-Conversational-Agent")
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
    
dataset = ChatDataSet()
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=num_workers)