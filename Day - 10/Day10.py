data = []
with open("Input.txt", "r") as f:
    for i in f.readlines():
        data.append([*i.strip()])    
f.close()

def points(x):
    if x == ')': return 3
    elif x == ']': return 57
    elif x == '}': return 1197
    else: return 25137

def pointsFill(l):
    c = 0
    while(l):
        c *= 5
        x = l.pop()
        if x == '(': c += 1
        elif x == '[': c += 2
        elif x == '{': c += 3
        else: c += 4
    return c

def corrupted(line, option): # option = True -> Part1 | option = False -> Part2
    l = []
    for i in line:
        if i in "([{<":
            l.append(i)
        elif (i == ')' and l[-1] == '(') or (i == ']' and l[-1] == '[') or (i == '>' and l[-1] == '<') or (i == '}' and l[-1] == '{'):
                l.pop()
        else:
            return points(i) if option else 0
    return 0 if option else pointsFill(l)

def getMiddle(l):
    l.sort()
    return l[int(len(l) / 2)]

def parts():
    c1 = 0
    c2 = 0
    l = []
    for i in data:
        c1 += corrupted(i, True)
        c2 = corrupted(i, False)
        if c2: l.append(c2)
    print("Part 1:", c1)
    print("Part 2:", getMiddle(l))

parts()