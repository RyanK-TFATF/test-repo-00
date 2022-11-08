# Insertion Sort Practice, Ryan Kelley
import random

list0 = []
x = 0

while x < 20:
    list0.append(random.randint(0,100)) 
    x += 1

def insertionSort(list):
    for i in range(1, len(list)):
        key = list[i]

        j = i - 1

        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j += -1
        list[j+1] = key
    
    return list

print(list0)
print(insertionSort(list0))
