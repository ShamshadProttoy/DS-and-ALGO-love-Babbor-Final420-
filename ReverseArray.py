def ReverseArray(A,start,end):
    while start<end:
        A[start],A[end]=A[end],A[start]

        start=start+1
        end=end-1


a=[1,2,3,4,5]
n=len(a)
ReverseArray(a,0,n-1)
print(a)

