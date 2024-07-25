import string
import random

array = "".join([random.choice(string.ascii_letters) for i in range(100)]).lower()
print(array.lower())
count = {}
max = 0
for i in range(len(array)):
    if array[i] in count:
        count[array[i]] = count[array[i]] + 1
        if max < count[array[i]]:
            max = count[array[i]]
    else:
        count[array[i]] = 1
print(count,"\n", max)
