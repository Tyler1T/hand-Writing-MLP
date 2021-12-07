
f = open("fc2bias.txt", "w")
for i in data1['fc2bias']:
    f.write(convert(i, 1, 15) + "\n")
f.close()

f = open("fc3bias.txt", "w")
for i in data2['fc3bias']:
    f.write(convert(i, 1, 15) + "\n")
f.close()


f = open("fc1_Weight.txt", "w")
for j in range(0, 50):
    for i in data3['fc1_Weight'][j]:
        f.write(convert(i, 1, 15) + "\n")
f.close()


f = open("fc2_Weight.txt", "w")
for j in range(0, 10):
    for i in data4['fc2_Weight'][j]:
        f.write(convert(i, 1, 15) + "\n")
f.close()

f = open("fc3_Weight.txt", "w")
for j in range(0, 10):
    for i in data5['fc3_Weight'][j]:
        f.write(convert(i, 1, 15) + "\n")
f.close()
# for i in data1['fc1_Weight'][49]:
#     print(i)
