def linear_search(a,n,x):
    for i in range(n):
        if(a[i]==x):
            return i
    return -1

data = [1,4,6,10,30,40]
x=10
n=len(data)
result=linear_search(data,n,x)
if(result==-1):
    print('Value not found in the list')
else:
    print(f'Value found! At the position of: {result+1}')
    

#time_complexity=O(n)
#space_complexity=O(1)
