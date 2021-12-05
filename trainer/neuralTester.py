import torch
import numpy as np
from torchvision import datasets
import torchvision.transforms as transforms
import torch.cuda as cuda
import torch.nn as nn
import torch.nn.functional as F
from torchsummary import summary

# number of subprocesses to use for data loading
num_workers = 0
# how many samples per batch to load
batch_size = 64

transform = transforms.ToTensor()

test_data = datasets.MNIST(root='data', train=False,
                                  download=True, transform=transform)

test_loader = torch.utils.data.DataLoader(test_data, batch_size=batch_size,
    num_workers=num_workers)

## Define the NN architecture
class NeuralNet(nn.Module):
    def __init__(self):
        super(NeuralNet, self).__init__()
        # linear layer 28*28 input into 16 nodes
        self.fc1 = nn.Linear(28 * 28, 50)

        # linear layer (n_hidden -> 10)
        self.fc2 = nn.Linear(50, 10)



    def forward(self, x):
        # flatten image input
        x = x.view(-1, 28 * 28)
        # add hidden layer, with relu activation function
        x = F.relu(self.fc1(x))

        x = self.fc2(x)

        return x

# initialize the NN
model = NeuralNet()

model = torch.load("model.pth")

# specify loss function
criterion = nn.CrossEntropyLoss()

# initialize lists to monitor test loss and accuracy
test_loss = 0.0
class_correct = list(0. for i in range(100))
class_total = list(0. for i in range(100))

# Set model to evaluation mode
model.eval()

for data, target in test_loader:
    # forward pass: compute predicted outputs by passing inputs to the model
    output = model(data)
    # calculate the loss
    loss = criterion(output, target)
    # update test loss
    test_loss += loss.item()*data.size(0)
    # convert output probabilities to predicted class
    _, pred = torch.max(output, 1)
    # compare predictions to true label
    correct = np.squeeze(pred.eq(target.data.view_as(pred)))
    # calculate test accuracy for each object class
    for i in range(batch_size):
        try:
          label = target.data[i]
          class_correct[label] += correct[i].item()
          class_total[label] += 1
        except IndexError:
          break

# calculate and print avg test loss
test_loss = test_loss/len(test_loader.dataset)
print('Test Loss: {:.6f}\n'.format(test_loss))

for i in range(10):
    if class_total[i] > 0:
        print('Test Accuracy of %5s: %2d%% (%2d/%2d)' % (
            str(i), 100 * class_correct[i] / class_total[i],
            np.sum(class_correct[i]), np.sum(class_total[i])))
    else:
        print('Test Accuracy of %5s: N/A (no training examples)' % (classes[i]))

print('\nTest Accuracy (Overall): %2d%% (%2d/%2d)' % (
    100. * np.sum(class_correct) / np.sum(class_total),
    np.sum(class_correct), np.sum(class_total)))
