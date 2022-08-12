x_cord = []
y_cord = []

with open("Input.txt", "r") as f:
    raw = f.readlines()
    for i in raw:
        i = i.strip().split(" ")
        x_cord.append((int(i[0].split(",")[0]), int(i[2].split(",")[0])))
        y_cord.append((int(i[0].split(",")[1]), int(i[2].split(",")[1])))

def function(data, x, option):
    t = [y_cord[x][0], y_cord[x][1]] if option else [x_cord[x][0], x_cord[x][1]]
    t.sort()
    for y in range(t[0], t[1] + 1):         
        if option: data[x_cord[x][0]][y] += 1
        else: data[y][y_cord[x][0]] += 1

def count(data):
    c = 0
    for i in range(1000):
        for j in range(1000):
            if data[i][j] >= 2:
                c += 1
    return c

def part1():
    data = [[0] * 1000 for i in range(1000)]
    for x in range(len(x_cord)):
        if(x_cord[x][0] == x_cord[x][1]):
            function(data, x, True)
        if(y_cord[x][0] == y_cord[x][1]):
            function(data, x, False)
    return count(data)

def part2():
    data = [[0] * 1000 for i in range(1000)]
    for x in range(len(x_cord)):
        a = x_cord[x][0] - x_cord[x][1]
        b = y_cord[x][0] - y_cord[x][1]
        if abs(a) == abs(b):
            for i in range(abs(a) + 1):
                data[x_cord[x][0] + i * (-1 if a >= 0 else 1)][y_cord[x][0] + i * (-1 if b >= 0 else 1)] += 1
        elif(x_cord[x][0] == x_cord[x][1]):
            function(data, x, True)
        elif(y_cord[x][0] == y_cord[x][1]):
            function(data, x, False)
    return count(data)

print("Part 1:", part1())
print("Part 2:", part2())
