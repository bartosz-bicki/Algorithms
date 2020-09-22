import random as r
import time
import matplotlib.pyplot as plt
import numpy as np

def insert(N): #this function inserts random numbers from 100 to 1000, repleced random() for more clear visualization
    lista = []
    for i in range(N-1):
        lista.append(r.randint(100, 1000))
    return lista

def quick_sort(lista): #quick sort algorithm. Chooses a pivot to sort smaller and bigger numbers
    if len(lista) <=1:
        return lista
    mark = lista[0]
    left=[]
    
    for x in lista:
        if x < mark:
            left.append(x)
    same=[]
    for x in lista:    
        if x == mark:
            same.append(x)
    right=[]
    for x in lista:
        if x > mark:
            right.append(x)
    
    return quick_sort(left) + same + quick_sort(right)

def selection_sort(lista): #selection sort algorithm. Chooses a place in list then looks for min value in others values.
    for i, n in enumerate(lista):
        j, m = min(enumerate(lista[i:]), key=lambda a: a[1])
        lista[j+i], lista[i] = n, m 
    return lista

def bubble_sort(lista): #bubble sort. Starting from end and compares with other values.
    for a in range(len(lista)):
        b = len(lista)-1
        while b>a:
            if lista[b] < lista[b-1]:
                hp = lista[b]
                lista[b]=lista[b-1]
                lista[b-1] = hp
            b-=1
    return lista

time_sort_quick=[]
time_sort_bubble=[]
time_sort_selection=[]
means={'Quick_mean': 0, 'Selection_mean':0, 'Bubble_mean':0}
sums={'Quick_sum':0, 'Selection_sum':0, 'Bubble_sum :':0} 
axis=np.linspace(100, 500, 400)

for i in range(100, 500):
    ex = insert(i)
    ex_1= insert(i)
    ex_2=insert(i)
    
    start = time.perf_counter()#starts timer
    selection_sort(ex)
    stop = time.perf_counter()#stops timer
    time_sort_selection.append(stop - start)#adds time to list 
    
    start = time.perf_counter()
    quick_sort(ex_1)
    stop = time.perf_counter()
    time_sort_quick.append(stop - start)
    
    start = time.perf_counter()
    bubble_sort(ex_2)
    stop = time.perf_counter()
    time_sort_bubble.append(stop - start)
    

means['Selection_mean'] = np.mean(time_sort_selection)  #adds value to a dictionary 
sums['Selection_sum'] = np.sum(time_sort_selection)
means['Quick_mean'] = np.mean(time_sort_quick)  
sums['Quick_sum'] = np.sum(time_sort_quick)
means['Bubble_mean'] = np.mean(time_sort_bubble)  
sums['Bubble_sum'] = np.sum(time_sort_bubble)  

fig, ax = plt.subplots(1, 3)
ax[0].plot(axis, time_sort_selection, label='Selection Sorting')
ax[0].plot(axis,time_sort_quick, label='Quick Sorting')
ax[0].plot(axis, time_sort_bubble,label='Bubble Sorting')
ax[1].bar(means.keys(), means.values(), label='mean')
ax[2].bar(sums.keys(), sums.values(), label='sums')
plt.show()

