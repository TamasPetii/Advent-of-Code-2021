data = []
with open("Input.txt", "r") as f:
    raw = f.readlines()
    for i in raw:
        i = i.strip().split()
        data.append((i[0], int(i[1])))
f.close()

# Part 1

depth = 0
horizontal = 0

for i in range(len(data)):
    if data[i][0] == "forward":
        horizontal += data[i][1]
    elif data[i][0] == "up":
        depth -= data[i][1]
    else:
        depth += data[i][1]

print("Part 1: " + str(depth * horizontal))

# Part 1

aim = 0
depth = 0
horizontal = 0

for i in range(len(data)):
    if data[i][0] == "forward":
        horizontal += data[i][1]
        depth += aim * data[i][1]
    elif data[i][0] == "up":
        aim -= data[i][1]
    else:
        aim += data[i][1]

print("Part 1: " + str(depth * horizontal))