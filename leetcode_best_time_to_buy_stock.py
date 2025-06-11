
prices=[7,6,4,3,1]
i,r = 0,1  
p = 0
while r < len(prices): 
    if prices[i] < prices[r]: 
        p = max(p,(prices[r]-prices[i]))   
    else: 
        i = r 
    r+=1
print(p)
 
