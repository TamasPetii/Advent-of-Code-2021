data = []
with open("Input.txt", "r") as f:
    for i in f.readlines():
        data.append([*i.strip()])    
f.close()

len_row = len(data[0])
len_data = len(data)

def lowPoint(x, y):
    for i in range(-1,2):
        for j in range(-1,2):
            if (i != 0 or j != 0) and len_data > x + i >= 0 and len_row > y + j >= 0 and int(data[x + i][y + j]) < int(data[x][y]):
                return False
    return True

def basinsSize(x,y):
    if data[x][y] != '9':
        basinsSize.counter += 1
        data[x][y] = '9'
        if len_data > x - 1 >= 0 and len_row > y  >= 0 and data[x - 1][y] != '9': basinsSize(x - 1,y)
        if len_data > x + 1 >= 0 and len_row > y  >= 0 and data[x + 1][y] != '9': basinsSize(x + 1,y)
        if len_data > x >= 0 and len_row > y + 1 >= 0 and data[x][y + 1] != '9':  basinsSize(x,y + 1)
        if len_data > x >= 0 and len_row > y - 1  >= 0 and data[x][y - 1] != '9': basinsSize(x,y - 1)
    return basinsSize.counter 

def part1():
    c = 0
    for i in range(len_data):
        for j in range(len_row):
            if data[i][j] != '9' and lowPoint(i, j):
                c += int(data[i][j]) + 1
    return c

def part2():
    maxs = []
    basinsSize.counter = 0
    for i in range(len_data):
        for j in range(len_row):
            if data[i][j] != '9':
                maxs.append(basinsSize(i,j))
                basinsSize.counter = 0
    maxs.sort(reverse=True)
    return maxs[0] * maxs[1] * maxs[2]



print("Part 1:", part1())
print("Part 2:", part2())