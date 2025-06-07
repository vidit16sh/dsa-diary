nums = [1,2,3,4] 
r = [] 
product = 1 
for i in nums: 
    product  *= i 
j = 0 
while j < len(nums): 
    r.append(int(product*(nums[j]**-1))) 
    j +=1  
return r 