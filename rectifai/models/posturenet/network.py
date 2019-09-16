import torch
import torch.nn as nn
import torch.nn.functional as F


# Hyperparameters
input_size = 17*2
hidden_sizes = [256,256]
n_classes = 2

class PostureNetwork(nn.Module):
    def __init__(self):
        super(PostureNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_sizes[0]) 
        self.fc2 = nn.Linear(hidden_sizes[0], hidden_sizes[1])  
        self.fc3 = nn.Linear(hidden_sizes[1], n_classes)  
        self.relu = nn.ReLU()

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        out = self.relu(out)
        out = self.fc3(out)

        return out