import hashlib
eingabe = "ckczppom"
count = 0
while True:
    if (hashlib.md5((eingabe + str(count)).encode('utf-8')).hexdigest())[0:6] == "000000":
        break
    count += 1
print(count)