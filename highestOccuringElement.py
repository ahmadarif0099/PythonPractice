import string
import random

array = "umar" #.join([random.choice(string.ascii_letters) for i in range(100)]).lower()
print(array.lower())
count = {}
maxi = 0
second_max = 0
for i in range(len(array)):
    if array[i] in count:
        count[array[i]] = count[array[i]] + 1
    else:
        count[array[i]] = 1
    if maxi < count[array[i]]:
        maxi = count[array[i]]
    elif second_max < count[array[i]] < maxi:
        second_max = count[array[i]]
print(count, "\n", maxi, second_max)
