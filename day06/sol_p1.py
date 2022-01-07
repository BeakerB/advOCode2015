with open('input.txt') as f:
    lines = f.readlines()

lines = [line.strip().split(' ') for line in lines]

n = 1000
a = [[False] * n for i in range(n)]

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
                a[i][k] = not a[i][k]
    #turn
    else:
        for i in range(x1, x2 + 1):
            for k in range(y1, y2 + 1):
                #on
                if line[1] == 'on':
                    a[i][k] = True
                #off
                else:
                    a[i][k] = False

#zählen
count = 0
for i in range(n):
    for k in range(n):
        if a[i][k]:
            count += 1
print(count)
