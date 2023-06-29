import matplotlib.pyplot as plt
import math
import time
import random
def bubblesort(l):
 # src: https://blog.finxter.com/daily-python-puzzle-bubble-sort/
 lst = l[:] # Work with a copy, don't modify the original
 for passesLeft in range(len(lst)-1, 0, -1):
    for i in range(passesLeft):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst
def qsort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    lesser = [x for x in lst[1:] if x <= pivot]
    greater = [x for x in lst[1:] if x > pivot]
    return qsort(lesser) + [pivot] + qsort(greater)

def timsort(l):
    # sorted() uses Timsort internally
    return sorted(l) 
def create_random_list(n):
    return random.sample(range(n), n)
 
n = 50000
xs = list(range(1,n,n//10))
y_bubble = []
y_qsort = []
y_tim = []
for x in xs:
    # Create list
    lst = create_random_list(x)
    
    # Measure time bubble sort
    start = time.time()

    bubblesort(lst)
    y_bubble.append(time.time()-start)
    # Measure time qsort
    start = time.time()
    qsort(lst)
    y_qsort.append(time.time()-start)
    # Measure time Timsort
    start = time.time()
    timsort(lst)
    y_tim.append(time.time()-start)
 
 
plt.plot(xs, y_bubble, '-x', label='Bubblesort')
plt.plot(xs, y_qsort, '-o', label='Quicksort')
plt.plot(xs, y_tim, '--.', label='Timsort')
plt.grid()
plt.xlabel('List Size (No. Elements)')
plt.ylabel('Runtime (s)')
plt.legend()
plt.savefig('alg_complexity_new.pdf')
plt.savefig('alg_complexity_new.jpg')
plt.show()