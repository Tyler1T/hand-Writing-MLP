import json
import os
import numpy as np


#Pulling weights and biases into their own array
with open("mnist_test.json", "r") as file:
    data0 = {
        "input":np.array(json.load(file)['image0']).tolist()
    }

def convert(n):
    return bin(n).replace("0b","").zfill(16)



f = open("input0.dat", "w")
f.truncate()
for i in data0['input']:
    f.write(convert(i) + "\n")
f.close()
