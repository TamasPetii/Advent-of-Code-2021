data = []
with open("Input.txt", "r") as f:
    raw = f.readlines()
    for i in raw:
        i = i.strip()
        data.append(int(i))
f.close()

# Part 1

c = 0
for i in range(len(data) - 1):
    if data[i] < data[i+1]: c += 1
print("Part 1: " + str(c))

# Part 2

c = 0
for i in range(len(data) - 3):
    if data[i] < data[i + 3]: c += 1
print("Part 2: " + str(c))