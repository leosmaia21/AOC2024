
file = "input"
data = ""
with open(file) as f:
    lines = []
    x = 0
    for line in f:
        x+=1
        data += line

starts = [i for i in range(len(data)) if data.startswith('mul(', i)]
print(len(starts))
ret = 0
d = []
for i in starts:
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
            print(l)
            ff = int(l[0])
            ss = int(l[1])
            d.append([i, ff, ss])
            ret += ff * ss

# do = [[i, "do"] for i in range(len(data)) if data.startswith('do()', i)]
# dont = [[i, "dont"] for i in range(len(data)) if data.startswith("don't()", i)]
# final = do + dont
# final = sorted(final, key=lambda x:x[0])
#
# print(final)
# for f in final:
#     if f[1] == "do":
#         ff = d[0][1]
#         ss = d[0][2]
#         ret+=ff*ss
#     d.pop(0)
# print(ret)
