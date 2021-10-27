import torch.nn as nn
import torch.nn.functional as F
from torchsummary import summary

## Define the NN architecture
class NeuralNet(nn.Module):
    def __init__(self):
        super(NeuralNet, self).__init__()
        # linear layer 28*28 input into 16 nodes
        self.fc1 = nn.Linear(28 * 28, 16)

        # linear layer (n_hidden -> 10)
        self.fc2 = nn.Linear(16, 10)

    def forward(self, x):
        # flatten image input
        x = x.view(-1, 28 * 28)
        # add hidden layer, with relu activation function
        x = F.relu(self.fc1(x))

        x = self.fc2(x)

        return x

# initialize the NN
model = NeuralNet()
summary(model, input_size=(1, 28, 28))
