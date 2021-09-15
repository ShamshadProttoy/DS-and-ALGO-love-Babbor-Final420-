def MoveNegEle(arr,n):
    left=0
    right=n-1
    mid=0
    while mid<=right:
        if arr[mid]<0:
            arr[mid],arr[left]=arr[left],arr[mid]
            mid=mid+1
            left=left+1
        elif arr[mid]==0:
            mid=mid+1
        else:
            arr[mid],arr[right]=arr[right],arr[mid]

            right=right-1

    return arr

arr=[2,5,0,0,-2,0,-8,5,9,-7]
n=len(arr)
print(n)
result=MoveNegEle(arr,n)
print(result)

