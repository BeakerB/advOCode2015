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

eingabe = open("day5_eingabe.txt", 'r')
count = 0
for zeile in eingabe:
    testString = (zeile.rstrip("\n"))
    if countvowels(testString) > 2 and doubleLetter(testString) and containing(testString):
        # print(testString)
        count += 1
print(count)

