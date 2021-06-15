def countvowels(string):
    num_vowels=0
    for char in string:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels+1
    return num_vowels

def doubleLetter(string):
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return True
    return False
    
def containing(string):
    for i in range(len(string) - 1):
        twoLetter = string[i] + string[i + 1]
        if twoLetter in ['ab', 'cd', 'pq', 'xy']:
            return False
    return True

def pairContaining(string):
    for i in range(len(string) - 3):
        twoLetter = string[i] + string[i + 1]
        for j in range(i + 2, len(string) - 1):
            compareLetter = string[j] + string[j + 1]
            if twoLetter == compareLetter:
                return True    
    return False

def repeatLetter(string):
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            return True
    return False

eingabe = open("day5_eingabe.txt", 'r')
count1 = count2 = 0
for zeile in eingabe:
    testString = (zeile.rstrip("\n"))
    if countvowels(testString) > 2 and doubleLetter(testString) and containing(testString):
        # print(testString)
        count1 += 1
    if pairContaining(testString) and repeatLetter(testString):
        count2 += 1
print(count1)
print(count2)

