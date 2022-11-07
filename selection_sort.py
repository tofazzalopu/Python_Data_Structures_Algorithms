def selection_sort(a,n):
    for step in range(n):
        min_index=step
        for i in range(step+1,n):
            if(a[i]<a[min_index]):
                min_index=i
        (a[min_index], a[step])=(a[step],a[min_index])
data= [2,230,2,5,80,40,25,3]
n=len(data)
selection_sort(data,n)
print('Organising the list in Ascending order: ')
print(data)



#time_complexity=O(n**2)
#space_complexity=O(1)