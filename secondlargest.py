import random

array = random.sample(range(1, 100), 10)
# iteration = input("which number do you want to print, e.g, second largest will take 2 as input: \n")
max = 0
second_largest = 0
for i in range(0, len(array)):
    if max < array[i]:
        max = array[i]

for i in range(0, len(array)):
    if second_largest < array[i] < max:
        second_largest = array[i]
print(array, second_largest)


