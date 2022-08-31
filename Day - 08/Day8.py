data = []
values = []
with open("Input.txt", "r") as f:
    raw = f.readlines()
    for i in raw:
        i = i.strip().split(" | ")
        data.append(i[0].split(" "))
        values.append(i[1].split(" "))
f.close()

def part1():
    counter = 0
    for i in values:
        for j in i:
            if len(j) == 2 or len(j) == 3 or len(j) == 7 or len(j) == 4:
                counter += 1
    return counter

def commonLetters(a, b):
    c = 0
    for i in a:
        if i in b:
            c += 1
    return c

def value(a, one, four):
    if len(a) == 2:
        return '1'
    elif len(a) == 4:
        return '4'
    elif len(a) == 3:
        return '7'
    elif len(a) == 7:
        return '8'
    elif len(a) == 5 and commonLetters(a, four) == 2:
        return '2'
    elif len(a) == 5 and commonLetters(a, one) == 2:
        return '3'
    elif len(a) == 5 and commonLetters(a, one) == 1:
        return '5'
    elif len(a) == 6 and commonLetters(a, one) == 1:
        return '6'
    elif len(a) == 6 and commonLetters(a, four) == 4:
        return '9'
    elif len(a) == 6 and commonLetters(a, four) == 3:
        return '0'

def find(data, length):
    for i in data:
        if len(i) == length:
            return i

def part2():
    c = 0
    for i in range(len(data)):
        s = ""
        for x in values[i]:
            s += value(x, find(data[i], 2), find(data[i], 4))
        c += int(s)
    return c


print("Part 1:", part1())
print("Part 2:", part2())