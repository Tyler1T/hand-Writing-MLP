import os

f = open("network.txt", "w")
for i in range(0, 200):
    f.write(f"neuron_layer1 n1_{i} (data, {i}, layer1_output[{i}]);\n")

f.write("\n")
for i in range(0, 50):
    f.write(f"neuron_layer2 n2_{i} (layer1_output, {i}, layer2_output[{i}]);\n")

f.write("\n")
for i in range(0, 10):
    f.write(f"neuron_layer3 n3_{i} (layer2_output, {i}, result[{i}]);\n")
