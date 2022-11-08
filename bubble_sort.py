def bubble_sort(a):
    for i in range(len(a)):
        for j in range(0,len(a)-i-1):
            if(a[j]>a[j+1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
data=[2,4,60,15,40,7,60,21,12]
bubble_sort(data)

print(f"sorted data in ascending order: {data}")


#time_complexity=O(n**2)
#space_complexity=O(1)

