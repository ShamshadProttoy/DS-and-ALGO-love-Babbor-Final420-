def uni(arr,brr,len1,len2):
    crr=[]
    k=0
    for i in range(0,len1):
        crr.append(arr[i])


    for i in range(0,len2):
        flag=0
        for j in range(0,len1):
            if arr[j]==brr[i]:
                flag=1


        if flag==0:
            crr.append(brr[i])

    return crr


def intrsc(arr,brr,len1,len2):
    crr=[]
    for i in range(0, len2):
        flag = 0
        for j in range(0, len1):
            if arr[j] == brr[i]:
                crr.append(brr[i])

    return crr


arr=[2,3,4,5,7,9]
brr=[1,3,9,12,15]
len1=len(arr)
len2=len(brr)
result=uni(arr,brr,len1,len2)
result1=intrsc(arr,brr,len1,len2)
print(result)
print(result1)





