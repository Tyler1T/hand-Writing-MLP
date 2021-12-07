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
def convert(n, q1, q2):
  
  if (n < 0):
    negFlag = 1
  else:
    negFlag = 0

  numberStr = str(n)
  pointIdx = numberStr.find('.')

  #Find integerb and fractionalbs
  integerb = numberStr[0 : pointIdx]
  fractionalb = '0.' + numberStr[pointIdx + 1 : ]

  bintegerb = str(bin(int(integerb)))
  ffractionalb = float(fractionalb)

  #Convert the binary integerb to a width of q1
  #Index of 'b'
  bIdx = bintegerb.find('b')
  bintegerb = bintegerb[bIdx + 1 :]
  
  #For positive numbers, go on including a '0' at the MSB
  while (len(bintegerb) < q1):
    bintegerb = '0' + bintegerb

  #Do the overflow.
  bintegerb = bintegerb[-q1:]
#   print(bintegerb, ".")
  #print(ffractionalb)

  #Fix up the binary fractionalb
  bfractionalb = ''
  for i in range(0, q2):
    k = 2*ffractionalb
    digit = int(k)
    bfractionalb = bfractionalb + str(digit)
    ffractionalb = k - int(k)

  

  if (negFlag): #if the decimal number is negative
    bintegerb, bfractionalb = twosComplement(bintegerb, bfractionalb, q1, q2)
    return bintegerb+"_"+bfractionalb
  else: # if the decimal number is positive
    return bintegerb+"_"+bfractionalb
  

def twosComplement(bintegerb, bfractionalb, q1, q2):
  bString = list(bintegerb + bfractionalb)

  #First, find 1's complement.
  for i in range(len(bString) - 1, -1, -1):
    if (bString[i] == '0'):
      bString[i] = '1'
    elif (bString[i] == '1'):
      bString[i] = '0'

  #Now, 2's complement.
  carry = '1'
  for i in range(len(bString) - 1, -1, -1):
    if carry == '0':
      break

    elif bString[i] == '0':
      bString[i] = carry
      carry = '0'
    
    elif bString[i] == '1':
      bString[i] = '0'

  return ''.join(bString[0:q1]), ''.join(bString[q1:])



f = open("fc1bias.txt", "w")
f.truncate()
for i in data0['fc1bias']:
    f.write(convert(i,2,14) + "\n")
f.close()


f = open("fc2bias.txt", "w")
f.truncate()
for i in data1['fc2bias']:
    f.write(convert(i,2,14) + "\n")
f.close()


f = open("fc1_Weight.txt", "w")
f.truncate()
for j in range(0, 50):
    for i in data2['fc1_Weight'][j]:
        f.write(convert(i,2,14) + "\n")
f.close()


f = open("fc2_Weight.txt", "w")
f.truncate()
for j in range(0, 10):
    for i in data3['fc2_Weight'][j]:
        f.write(convert(i,2,14) + "\n")
f.close()
