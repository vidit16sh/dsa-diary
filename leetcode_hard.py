if len(s) < len(t):  
           return "" 
    if t == "":
           return ""       
   
    h1, h2 = {}, {} 
    m = len(s) + 1 
    start = end = 0  # to store final window
   
       for c in t: 
           h1[c] = 1 + h1.get(c, 0) 
   
       e1, e2 = len(h1), 0 
       l = 0        
   
       for r in range(len(s)): 
           h2[s[r]] = 1 + h2.get(s[r], 0)  
   
           if s[r] in h1 and h2[s[r]] == h1[s[r]]:
               e2 += 1 
   
           while e1 == e2: 
               if (r - l + 1) < m: 
                   m = r - l + 1   
                   start, end = l, r

               # ✅ check before decreasing
               if s[l] in h1 and h2[s[l]] == h1[s[l]]:
                   e2 -= 1
               h2[s[l]] -= 1
               l += 1    
return s[start : end + 1] if m != (len(s) + 1) else ""