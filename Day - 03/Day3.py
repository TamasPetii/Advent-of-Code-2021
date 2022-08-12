data = []
with open("Input.txt", "r") as f:
    raw = f.readlines()
    for i in raw:
        i = i.strip()
        data.append(i)
f.close()

def fun(data, ind):
    c = 0
    for i in range(len(data)):
        c += int(data[i][ind])
    return c

def decimal(occure, mostCommon):
    string = ""
    for i in occure:
        if i  >= len(data) / 2:
            if mostCommon: string += "1"
            else: string += "0"
        else:
            if mostCommon: string += "0"
            else: string += "1"
    return int(string, 2)

# Part 1

occure = [0] * len(data[0])

for i in range(len(data[0])):
    occure[i] = fun(data, i)

print(decimal(occure, True) * decimal(occure, False))

#Part 2

def rec(option):
    datalist = data.copy()
    ind = 0
    while(len(datalist) != 1):
        if option:
            c = 1 if fun(datalist, ind) >= len(datalist) / 2 else 0 
        else:
            c = 0 if fun(datalist, ind) >= len(datalist) / 2 else 1 

        l = []
        for i in range(len(datalist)):
            if int(datalist[i][ind]) == c:
                l.append(datalist[i])
        datalist = l

        ind += 1
    return datalist[0]
print(int(rec(True), 2), int(rec(False), 2))
print(int(rec(True), 2) * int(rec(False), 2))