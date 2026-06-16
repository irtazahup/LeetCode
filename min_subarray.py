def MinSubArray(arr,target):
    i=0
    j=i
    min_len=float('inf')
    sum=0
    while i < len(arr):
        
        while sum < target and j < len(arr):
            sum+=arr[j]
            j+=1
       
        if sum >= target:
            min_len=min(min_len,j-i)
       
        
        sum=0
        i+=1
        j=i
    return min_len


print(MinSubArray([1,2,3,4,5],15)) 
    
    