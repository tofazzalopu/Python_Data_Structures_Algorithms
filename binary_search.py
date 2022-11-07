def binary_search(a,n,x):
    left=0
    right=n-1
    for i in range(0,n):
        if(left<=right):
            mid=int((left+right)/2)
            if(a[mid]==x):
                return mid
            elif(a[mid]<x):
                left=mid+1
            elif(a[mid]>x):
                right=mid-1
    return -1

data=[2,4,6,8,10,14,19,22,25,30]
n=len(data)
x=14
result=binary_search(data,n,x)
if(result==-1):
    print('Value not found in the list')
else:
    print(f'Value found! At the position of: {result+1}')


#time_complexity=O(logN)
#space_complexity=O(1)