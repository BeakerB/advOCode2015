with open('input.txt') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

hexDigit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
sumOfAllChars = 0
clearedSum = 0

for line in lines:
    diff = 0
    sumOfAllChars += len(line)
    line = line[1:-1]
    clearedSum += len(line)
    for i in range(len(line[:-3])):
        if line[i] == '\\' and line[i + 1] == 'x' and line[i + 2] in hexDigit and line[i + 3] in hexDigit:
            diff += 3
    clearedSum -= diff
    diff = 0
    for i in range(len(line[:-1])):
        if line[i] == '\\' and line[i + 1] == '\\':
            diff += 1
    clearedSum -= diff
    diff = 0
    for i in range(len(line[:-1])):
        if line[i] == '\\' and line[i + 1] == '"':
            diff += 1
    clearedSum -= diff
    diff = 0

print(sumOfAllChars, clearedSum, sumOfAllChars - clearedSum)
