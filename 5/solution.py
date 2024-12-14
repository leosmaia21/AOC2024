
data1 = []
data2 = []
file = "input"
newline= 0
with open(file) as f:
    for line in f:
        if line == "\n": newline = 1
        if newline == 0:
            l = line.split("|")
            data1.append((int(l[0]), int(l[1])))
        else:
            l = line.split(",")
            data2.append([int(x) for x in l])

ret = []

for l2 in data2:
    for id2, d2 in enumrate(l2):
        ok = 1
        aux=[]
        for i in range(len(data1)):
            if d2 == data1[i][0] or d2 == data1[i][1]:
                aux.append(data1[i])
        for id1 in range(id2, len(l2)):
            for a in aux:
                if a[0] == d2[0]:

                    first = True
                if a[1] == d2[0]:














