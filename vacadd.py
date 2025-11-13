def dotProduct(l1, l2):
    len1 = len(l1)
    len2 = len(l2)
    
    if(len1 > len2):
        Minimum = len2
    else:
        Minimum = len1  
          
    sum = 0
    for i in range (0,Minimum):
        sum+=l1[i]*l2[i]
        
    return sum

print(dotProduct([2,3], [3,4,5]))

