 # import libraries
import torch
import numpy as np
from torchvision import datasets
import torchvision.transforms as transforms
import torch.cuda as cuda
import torch.nn as nn
import torch.nn.functional as F
from torchsummary import summary
import json


torch.set_default_tensor_type('torch.cuda.FloatTensor')
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


# number of subprocesses to use for data loading
num_workers = 0
# how many samples per batch to load
batch_size = 16

# convert data to torch.FloatTensor
transform = transforms.ToTensor()

# choose the training and test datasets
train_data = datasets.MNIST(root='data', train=True,
                                   download=True, transform=transform)
test_data = datasets.MNIST(root='data', train=False,
                                  download=True, transform=transform)

# prepare data loaders
train_loader = torch.utils.data.DataLoader(train_data, batch_size=batch_size,
    num_workers=num_workers)
test_loader = torch.utils.data.DataLoader(test_data, batch_size=batch_size,
    num_workers=num_workers)


## Define the NN architecture
class NeuralNet(nn.Module):
    def __init__(self):
        super(NeuralNet, self).__init__()
        # linear layer 28*28 input into 16 nodes
        self.fc1 = nn.Linear(28 * 28, 50)
        self.fc1.to(device)

        # linear layer (n_hidden -> 10)
        self.fc2 = nn.Linear(50, 10)
        self.fc2.to(device)



    def forward(self, x):
        # flatten image input
        x = x.view(-1, 28 * 28)
        # add hidden layer, with relu activation function
        x = F.relu(self.fc1(x))

        x = self.fc2(x)

        return x

# initialize the NN
model = NeuralNet().to(device)
summary(model, input_size=(1, 28, 28))

## Specify loss and optimization functions

# specify loss function
criterion = nn.CrossEntropyLoss()

# specify optimizer
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)

# number of epochs to train the model
n_epochs = 1  # suggest training between 20-50 epochs

# Set model to the training mode
model.train()

for epoch in range(n_epochs):
    # monitor training loss
    train_loss = 0.0

    ###################
    # train the model #
    ###################
    for data, target in train_loader:
        data, target = data.to(device), target.to(device)

        # clear the gradients of all optimized variables
        optimizer.zero_grad()
        # forward pass: compute predicted outputs by passing inputs to the model
        output = model(data)

        # calculate the loss
        loss = criterion(output, target)
        # backward pass: compute gradient of the loss with respect to model parameters
        loss.backward()
        # perform a single optimization step (parameter update)
        optimizer.step()
        # update running training loss
        train_loss += loss.item()*data.size(0)

    # print training statistics
    # calculate average loss over an epoch
    train_loss = train_loss/len(train_loader.dataset)

    print('Epoch: {} \tTraining Loss: {:.6f}'.format(
        epoch+1,
        train_loss
        ))

# initialize lists to monitor test loss and accuracy
test_loss = 0.0
class_correct = list(0. for i in range(10))
class_total = list(0. for i in range(10))

# Set model to evaluation mode
model.eval()

for data, target in test_loader:
    data, target = data.to(device), target.to(device)

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

model.cpu()

torch.save(model, 'model.pth')

bias_hidden = model.fc1.bias.data.numpy()
bias_output = model.fc2.bias.data.numpy()

weight_hidden = model.fc1.weight.data.numpy()
weight_output = model.fc2.weight.data.numpy()


#Combining all Weights and Biases
data = {

    "fc1bias":np.array(bias_hidden, dtype="float32").tolist(),
    "fc2bias":np.array(bias_output, dtype="float32").tolist(),
    "fc1_Weight":np.array(weight_hidden, dtype="float32").tolist(),
    "fc2_Weight":np.array(weight_output, dtype="float32").tolist()
}
# Storing Biases
data0 = {
    "fc1bias":np.array(bias_hidden, dtype="float32").tolist(),
}

data1 = {
    "fc2bias":np.array(bias_output, dtype="float32").tolist()
}
# Storing Weights
data2 = {
    "fc1_Weight":np.array(weight_hidden, dtype="float32").tolist(),
}
data3 = {
    "fc2_Weight":np.array(weight_output, dtype="float32").tolist()
}

#Storing all weights and biases in one file
with open("weight_bias_combined.json", "w") as file:
    json.dump(data,file,indent = 1)

#Storing weights and biases in their own files
with open("fc1bias.json", "w") as file:
    json.dump(data0,file,indent = 1)
with open("fc2bias.json", "w") as file:
    json.dump(data1,file,indent = 1)
with open("fc1_Weight.json", "w") as file:
    json.dump(data2,file,indent = 1)
with open("fc2_Weight.json", "w") as file:
    json.dump(data3,file,indent = 1)
