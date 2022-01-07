with open('test.txt', encoding='utf-8') as f:
    lines = f.readlines()

lines = [line.strip().split(' ') for line in lines]

wires = {}
kill = []

for line in lines:
    for i in range(len(line)):
        if line[i] == '->':
            wires[line[i + 1]] = -1

for line in lines:
    if line[1] == '->':
        try:
            wert = int(line[0])
        except ValueError:
            wert = wires[line[0]]
        if wert != -1:
            wires[line[2]] = wert
            kill.append(line)

    elif line[1] in ['AND', 'OR', 'LSHIFT', 'RSHIFT']:
        try:
            wert1 = int(line[0])
        except ValueError:
            wert1 = wires[line[0]]
        try:
            wert2 = int(line[2])
        except ValueError:
            wert2 = wires[line[2]]
        if wert1 != -1 and wert2 != -1:
            if line[1] == 'AND':
                wires[line[4]] = wert1 & wert2
            elif line[1] == 'OR':
                wires[line[4]] = wert1 | wert2
            elif line[1] == 'LSHIFT':
                wires[line[4]] = wert1 << wert2
            elif line[1] == 'RSHIFT':
                wires[line[4]] = wert1 >> wert2
            kill.append(line)
    elif line[0] == 'NOT':
        try:
            wert = int(line[1])
        except ValueError:
            wert = wires[line[1]]
        if wert != -1:
            if ~wert < 0:
                wires[line[3]] = 65536 + (~wert)
            else:
                wires[line[3]] = ~wert
            kill.append(line)
for line in kill:
    lines.remove(line)
kill.clear()

print(lines)
print(wires)
print(wires['a'])
