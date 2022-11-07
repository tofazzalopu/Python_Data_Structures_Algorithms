#Linear_Search
# def linear_search(a,n, x):
    
#     for i in range(0,n):
#         if(a[i]==x):
#             return i
#     return -1

# a=[10,14,39,20,49,30]
# x=39
# n = len(a)
# result=linear_search(a,n,x)
# if(result ==-1):
#     print("Pai nai")
# else:
#     print(f'paici at the position of {result+1}')



# def main():
#     n = int(input("Enter Looping Phase: "))
#     count = 0
#     i=0
#     j=0
#     for i in range(n):
#         for j in range(n):
#             count = count+1
#     print(f"n = {n}, count = {count}")
#     return 0

# main()

# #Binary_Search
# def binary_search(a,n,x):
#     left = 0
#     right = n-1
#     for i in range(0,n):
#         if(left<=right):
#             mid=int((left+right)/2)
#             if(a[mid]==x):
#                 return mid
#             elif(a[mid]<x):
#                 left=mid+1          
#             elif(a[mid]>x):
#                 right=mid-1
#     return -1
# a=[10,20,30,40,50,70,90]
# x=70
# n=len(a)
# result=binary_search(a,n,x)
# if(result==-1):
#     print ('number nai')
# else:
#     print(f"Number is here at the position of: {result+1}")


#Selection_sort
def selection_sort(a,size):
    
    for step in range(size):
        index_min=step
        for i in range(step+1, size):
            if(a[i]<a[index_min]):
                index_min=i
        (a[step], a[index_min])=(a[index_min],a[step])
data=[2,5,30,32,21,10,5,6]
size=len(data)
selection_sort(data,size)
print(data)
