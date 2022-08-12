data = [0] * 9
with open("Input.txt", "r") as f:
    raw = f.readline().strip().split(",")
    for i in raw:
        data[int(i)] += 1
f.close()

def simulation(time, data):
    for i in range(time):
        new = data[0]
        data = data[1:] + [new]
        data[6] += new
    return sum(data)

print("Part 1:",simulation(80, data.copy()))
print("Part 2:",simulation(256, data.copy()))