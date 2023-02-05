# Sort Practice, Ryan Kelley,  v0.0 
import random


list0 = []
x = 0

while x < 50:
    list0.append(random.randint(0,100)) 
    x += 1

print (list0)

list1 = []
y = 0

while y < 50:
    list1.append(random.randint(0,100)) 
    y += 1

print(list1)


def bubble_sort_ascend(list):
    n = len(list)

    for i in range(n-1):
        for j in range(n-i-1):
            if (list[j] > list[j+1]):
                list[j], list[j+1] = list[j+1], list[j]
    return list 

def bubble_sort_descend(list):
    n = len(list)

    for i in range(n-1):
        for j in range(n-i-1):
            if (list[j] < list[j+1]):
                list[j+1], list[j] = list[j], list[j+1]
    return list 

print (bubble_sort_ascend(list0))
print (bubble_sort_descend(list1))