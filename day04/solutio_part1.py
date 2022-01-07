import hashlib
import sys

INPUT = "bgvyzdsv"
ok = False
count = 0

while not ok:
    test = INPUT + str(count)
    hash_object = hashlib.md5(test.encode())
    md5_hash = hash_object.hexdigest()
    aus = str(md5_hash[0:6])
    print(md5_hash, count, aus)
    if aus == '000000':
        print('gefunden!!!')
        ok = True
    count += 1
