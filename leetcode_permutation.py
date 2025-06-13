s1 = 'ab' 
s2 = 'efabcd' 
h1,h2 = [0]*26,[0]*26 
for i in range(len(s1)): 
    h1[ord(s1[i])-ord('a')] += 1 
    h2[ord(s2[i])-ord('a')] += 1 
if s1 == s2: 
    print(True) 
l,r = 0,len(s1) 
while r < len(s2): 
    h2[ord(s2[r])-ord('a')] +=1 
    h2[ord(s2[l])-ord('a')] -=1 
    if h2 == h1: 
        print(True) 
    r+=1 
    l+=1 

     

