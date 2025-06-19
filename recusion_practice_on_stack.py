stack = [1,2,3,4,5,6] 

# k = int(len(stack)/2) + 1
# def md(stack,k): 
#     if not stack:  
#         return 
#     if k == 1: 
#         stack.pop() 
#         return  
#     temp = stack.pop() 
#     md(stack,k-1) 
#     stack.append(temp) 
# md(stack,k) 
# print(stack) 
def revs(stack): 
    if not stack or len(stack) == 1: 
        return 
    item = stack.pop() 
    revs(stack) 
    ins(stack,item)   
def ins(stack,item): 
    if not stack: 
        stack.append(item)  
        return 
    temp = stack.pop() 
    ins(stack,item) 
    stack.append(temp)
revs(stack) 
print(stack)