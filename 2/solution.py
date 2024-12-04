
data = []
file = "input"
with open(file) as f:
    for line in f:
        data.append([int(x) for x in line.split()])


ret = 0
safes = []
for i, line in enumerate(data):
    incre = 0
    if line[0] < line[1]:
        incre = 1
    ok = 1
    for c in range(len(line) - 1):
        if line[c] == line[c+1]:
            ok = 0
        if line[c] > line[c + 1] and incre == 1:
            ok = 0
        if line[c] < line[c + 1] and incre == 0:
            ok = 0
        a = abs(line[c] - line[c+1])
        if a<0 or a>=4:
            ok = 0
    if ok == 1:
        safes.append(i)
        ret+=1

for i, line in enumerate(data):
    if i in safes: continue
    for n in range(len(line)):
        newline = line.copy()
        newline.pop(n)
        print(newline, n)
        incre = 0
        if newline[0] < newline[1]:
            incre = 1
        ok = 1
        removed = 0
        for c in range(len(newline) - 1):
            if newline[c] == newline[c+1]:
                ok = 0
            if newline[c] > newline[c + 1] and incre == 1:
                ok = 0
            if newline[c] < newline[c + 1] and incre == 0:
                ok = 0
            a = abs(newline[c] - newline[c+1])
            if a<0 or a>=4:
                ok = 0
        if ok == 1:
            ret+=1
            break
print(ret)
