def insertion_sort(a):
    for i in range(1,len(a)):
        item = a[i]
        j=i-1
        while j>=0 and item<a[j]:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=item

data = [10,5,6,8,7,20,30,25,40,60]
data.append(4)
insertion_sort(data)
print(data)
        

#time_complexity=O(n**2)
#space_complexity=O(1)