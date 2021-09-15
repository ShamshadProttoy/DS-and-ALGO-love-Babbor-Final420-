def sort123(arr,size):
    low=0
    high=size-1
    mid=0
    while mid<=high:
        if arr[mid]==0:
            arr[mid],arr[low]=arr[low],arr[mid]
            mid=mid+1
            low=low+1

        elif arr[mid]==1:
            mid=mid+1

        else:
            arr[mid],arr[high]=arr[high],arr[mid]

            high=high-1
    return arr

arr=[2,1,1,0,1,2,2,0,0]
n=len(arr)
sorted=sort123(arr,n)
print(sorted)
