# TODO: BINARY SEARCH RECURSIVE

def binary_search_helper(arr , val , low , high) :
    if low>high:
        return "No Match"
    
    mid =low + ((high-low)//2)

    if arr[mid] == val :
        return mid
    elif val > arr[mid]:
        return binary_search_helper(arr,val,mid+1,high)
    else:
        binary_search_helper(arr,val,low,mid-1)
    
def binary_search(arr,val):
    return binary_search_helper(arr,val,0,len(arr)-1)

arr=[1,2,3,4,5,6,7,8]
print("Value found at index: ",binary_search(arr,4))
print("Value found at: ",binary_search(arr,14))