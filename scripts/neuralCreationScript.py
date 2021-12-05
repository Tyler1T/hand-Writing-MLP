import os

f = open("network.txt", "w")

for i in range(0, 50):
    f.write(f"neuron_layer1 n{i} (data[767:0], {i});\n")
