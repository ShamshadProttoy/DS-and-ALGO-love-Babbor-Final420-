class pair:
    def __init__(self):
        self.max=0
        self.min=0


def getMaxMin(arr,n)-> pair:
    minmax=pair()

    if n==1:
        minmax.min=arr[0]
        minmax.max=arr[0]
        return minmax
    if arr[0]>arr[1]:
        minmax.max=arr[0]
        minmax.min=arr[1]
    else:
        minmax.max = arr[1]
        minmax.min = arr[0]

    for i in range(2,n):
        if arr[i]>minmax.max:
                 minmax.max=arr[i]

        elif arr[i]<minmax.min:
               minmax.min=arr[i]
    return minmax

arr=[4,6,9,6,10,8,8]
n=len(arr)
minmax=getMaxMin(arr,n-1)
print("maximun=",minmax.max)

print("minimum=",minmax.min)





