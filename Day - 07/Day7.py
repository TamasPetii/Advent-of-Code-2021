data = []
with open("Input.txt", "r") as f:
    raw = f.readline().strip().split(",")
    for i in raw:
        data.append(int(i))
f.close()

def fuel(x, option):
    f = 0
    for i in data:
        y = abs(i - x)
        if option: f += y
        else: f += y * (y + 1) / 2
    return int(f)

minimum_p1 = fuel(1, True)
minimum_p2 = fuel(1, False)
for i in range(2, max(data)):
    minimum_p1 = min(fuel(i, True), minimum_p1)
    minimum_p2 = min(fuel(i, False), minimum_p2)

print("Part 1:", minimum_p1)
print("Part 2:", minimum_p2)