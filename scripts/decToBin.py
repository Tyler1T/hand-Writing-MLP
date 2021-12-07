import json
import os
import numpy as np
from float2fixed import convert

#Pulling weights and biases into their own array
with open("fc1bias.json", "r") as file:
    data0 = {
        "fc1bias":np.array(json.load(file)['fc1bias']).tolist()
    }
with open("fc2bias.json", "r") as file:
    data1 = {
        "fc2bias":np.array(json.load(file)['fc2bias']).tolist()
    }
with open("fc3bias.json", "r") as file:
    data2 = {
        "fc3bias":np.array(json.load(file)['fc3bias']).tolist()
    }

with open("fc1_Weight.json", "r") as file:
    data3 = {
        "fc1_Weight":np.array(json.load(file)["fc1_Weight"]).tolist()
    }
with open("fc2_Weight.json", "r") as file:
    data4 = {
        "fc2_Weight":np.array(json.load(file)["fc2_Weight"]).tolist()
    }
with open("fc3_Weight.json", "r") as file:
    data5 = {
        "fc3_Weight":np.array(json.load(file)["fc3_Weight"]).tolist()
    }


f = open("fc1bias.txt", "w")
for i in data0['fc1bias']:
    f.write(convert(i, 1, 15) + "\n")
f.close()
