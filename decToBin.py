import json
import os
import numpy as np


#Pulling weights and biases into their own array
with open("fc1bias.json", "r") as file:
    data0 = {
        "fc1bias":np.array(json.load(file)['fc1bias']).tolist()
    }
with open("fc2bias.json", "r") as file:
    data1 = {
        "fc2bias":np.array(json.load(file)['fc2bias']).tolist()
    }
with open("fc1_Weight.json", "r") as file:
    data2 = {
        "fc1_Weight":np.array(json.load(file)["fc1_Weight"]).tolist()
    }
with open("fc2_Weight.json", "r") as file:
    data3 = {
        "fc2_Weight":np.array(json.load(file)["fc2_Weight"]).tolist()
    }

def convert(num):
    num_original = num
    num_mag = abs(num)

    bin = list("")

    if(num_mag - 1 < 0):
        bin.append("0")
    else:
        bin.append("1")
        num =- 1

    for i in range(0, 15):
        if(num_mag - 2**-i < 0):
            bin.append("0")
        else:
            bin.append("1")
            num_mag =- 2**-i

    if(num_original < 0):
        for i in range(0, 15):
            if(bin[i] == '1'): bin[i] = '0'
            else: bin[i] = '1'

        carry = 1
        for i in range(0, 15):
            if(bin[i] == '1' and carry == 0):
                bin[i] = '1'
            elif(bin[i] == '1' and carry == 1):
                bin[i] = '0'
                carry = 0
            elif(bin[i] == '0' and carry == 1):
                bin[i] = '1'
                carry = 0
            else: bin[i] = '0'

    return "".join(bin)



f = open("fc1bias.txt", "a")
f.truncate()
for i in data0['fc1bias']:
    f.write(convert(i) + "\n")
f.close()


f = open("fc2bias.txt", "a")
f.truncate()
for i in data1['fc2bias']:
    f.write(convert(i) + "\n")
f.close()


f = open("fc1_Weight.txt", "a")
f.truncate()
for j in range(0, 50):
    for i in data2['fc1_Weight'][j]:
        f.write(convert(i) + "\n")
f.close()


f = open("fc2_Weight.txt", "a")
f.truncate()
for j in range(0, 10):
    for i in data3['fc2_Weight'][j]:
        f.write(convert(i) + "\n")
f.close()
# for i in data1['fc1_Weight'][49]:
#     print(i)
