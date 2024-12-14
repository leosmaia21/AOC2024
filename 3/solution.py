
file = "input"
data = ""
with open(file) as f:
    lines = []
    x = 0
    for line in f:
        x+=1
        data += line

starts = [i for i in range(len(data)) if data.startswith('mul(', i)]
do = [i for i in range(len(data)) if data.startswith('do()', i)]
dont = [i for i in range(len(data)) if data.startswith("don't()", i)]
ret = 0
d = []
go = True
dontindex = 0
doindex = 0
ite= True
do.insert(0, 0)
dont.append(1000000000)
do.append(1000000000)
for index, i in enumerate(starts):
    if do[0] <i:
        go = True
        do.pop(0)
    if dont[0] <i:
        go = False
        dont.pop(0)


    if go:
        s = data[i:i+13]
        first = 0
        second = 0
        comma =0
        paren = 0
        for index, e in enumerate(s[4:]):
            if not e.isdigit() and e != ","  and e != ")":
                break
            if e.isdigit() and second == 0 and comma == 0 and paren==0:
                first+=1
            elif e == ',' and first != 0 and second == 0 and comma == 0:
                comma = index + 4
            elif e.isdigit() and first != 0 and comma != 0:
                second+=1
            elif e == ')' and first != 0 and second != 0 and comma != 0:
                paren = 1
                break
        if paren == 1:
            if first < 4 and second <4 and paren == 1 and comma != 0:
                l = s[4:].split(")")[0].split(",")
                ff = int(l[0])
                ss = int(l[1])
                d.append([i, ff, ss])
                print(ff, ss)
                ret += ff * ss
print(ret)
