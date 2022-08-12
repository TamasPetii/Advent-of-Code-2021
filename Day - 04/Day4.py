numbers = []
data = []

with open("Input.txt", "r") as f:
    numbers = f.readline().strip().split(",")
    while True:
        buf = f.readline()
        if not buf:
            break

        l = []
        for i in range(5):
            l += list(filter((''.__ne__), f.readline().strip().split(" ")))
        data.append(l)  
        
f.close()

def bingo(matrix):
    for i in range(5):
        if matrix[0 + i * 5] + matrix[1 + i * 5] + matrix[2 + i * 5] + matrix[3 + i * 5] + matrix[4 + i * 5] == 5:
            return True
        if matrix[0 + i] + matrix[5 + i] + matrix[10 + i] + matrix[15 + i] + matrix[20 + i] == 5:
            return True
    return False

def result(data, matrix, num):
    c = 0
    for i in range(len(data)):
        if matrix[i] == 0: 
            c += int(data[i])
    return c * int(num)


def function(data):
    matrix = [0] * 25
    for i in range(len(numbers)):
        if numbers[i] in data:
            matrix[data.index(numbers[i])] = 1
            if bingo(matrix):     
                return (i,result(data, matrix, numbers[i]))


for i in range(len(data)):
    current = function(data[i])
    if i == 0:
        maximum = current
        minimum = current
    else:
        if current[0] > maximum[0]: maximum = current
        if current[0] < minimum[0]: minimum = current

print("Part 1: " + str(minimum[1]))
print("Part 2: " + str(maximum[1]))