def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

my_arr=[40,20,50,60,30,10]
bubble_sort(my_arr)

for i in my_arr:
    print(i,end=" ")