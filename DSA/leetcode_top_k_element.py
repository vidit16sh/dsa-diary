nums = [1,1,2,2,3]
d = {} 
k = 2
for i in nums: 
    if i not in d : 
        d[i] = 1  
    else : 
        d[i]+=1 
l = sorted(d.items(),key=lambda item:item[1],reverse= True) 
for i in range(k): 
    print(l[i][0]) 
