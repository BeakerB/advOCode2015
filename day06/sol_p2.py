with open('input.txt') as f:
    lines = f.readlines()

lines = [line.strip().split(' ') for line in lines]

n = 1000
a = [[0] * n for i in range(n)]

for line in lines:
    #koordinaten
    x1 = int(line[-3:-2][0].split(',')[0])
    y1 = int(line[-3:-2][0].split(',')[1])
    x2 = int(line[-1:][0].split(',')[0])
    y2 = int(line[-1:][0].split(',')[1])

    #toggle
    if line[0] == 'toggle':
        for i in range(x1, x2 + 1):
            for k in range(y1, y2 + 1):
                a[i][k] += 2
    #turn
    else:
        for i in range(x1, x2 + 1):
            for k in range(y1, y2 + 1):
                #on
                if line[1] == 'on':
                    a[i][k] += 1
                #off
                else:
                    if a[i][k] > 0:
                        a[i][k] -= 1

#zählen
count = 0
for i in range(n):
    for k in range(n):
        count += a[i][k]
print(count)
