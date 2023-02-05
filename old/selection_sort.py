# Selection Sort 
import random

list0 = []
x = 0

while x < 20:
    list0.append(random.randint(0,100)) 
    x += 1

def selectionSort(list):
    for i in range(len(list)):
        minimum_index = i
        for j in range (i+1, len(list)):
            if list[minimum_index] > list[j]:
                minimum_index = j

        list[i], list[minimum_index] = list[minimum_index], list[i]

    return list

print (list0)
print (selectionSort(list0))