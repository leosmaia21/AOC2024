
data = []
file = "input"
with open(file) as f:
    for line in f:
        line = line.strip()
        data.append([c for c in "0000" + line + "0000"])

width = len(data[0])
height = len(data)  + 8
line = [[c for c in "0" * width]] * 4
data = line + data + line
xmas = ["XMAS", "SAMX"]
ret = 0
# for y in range(0, height -3):
#     for x in range(0, width -3):
#         horizontal = data[y][x] + data[y][x+1] + data[y][x+2] + data[y][x+3]
#         vertical = data[y][x] + data[y+1][x] + data[y+2][x] + data[y+3][x]
#         diagonall = data[y][x] + data[y+1][x+1] + data[y+2][x+2] + data[y+3][x+3]
#         diagonalr = data[y][x] + data[y+1][x-1] + data[y+2][x-2] + data[y+3][x-3]
#         i = 0
#         if horizontal in xmas:
#             i =1
#             ret+=1
#         if vertical in xmas:
#             i =1
#             ret+=1
#         if diagonall in xmas:
#             i =1
#             ret+=1
#         if diagonalr in xmas:
#             i =1
#             ret+=1


print(ret)

ret = 0
xmas = ['MAS', 'SAM']
for l in data:
    print(l)
for y in range(3, height -3):
    for x in range(3, width -3):
        i = 0
        if data[y][x] == 'A':
            diagonalr = data[y-1][x-1] + data[y][x] + data[y+1][x+1]
            diagonall = data[y-1][x+1] + data[y][x] + data[y+1][x-1]
            if diagonall in xmas and diagonalr in xmas:
                print(x-4, y-4)
                ret+=1
                i =1

print(ret)
