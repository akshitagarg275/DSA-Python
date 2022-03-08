def insertion_sort(arr):
    for i in range(len(arr)):
        min_idx=i
        for j in range(i+1,len(arr)):
            if arr[min_idx]>arr[j]:
                #we need to find smallest element in remainig arr
                # that's why we will be swapping at last
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]


my_arr=[5,4,1,8,3]
insertion_sort(my_arr)

for i in my_arr:
    print(i,end=" ")