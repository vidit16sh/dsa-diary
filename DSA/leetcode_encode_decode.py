def encode(strs): 
     f = ""
     for k in strs:  
          f += str(len(k)) + '$' + k 
     return f
def decode(s): 
     fstr = [] 
     i = 0 
     while i < len(s): 
        j = i
        while s[j] != '$': 
            j = j + 1 
        l = int(s[i:j]) 
        i = j + 1  
        fstr.append(s[i:i+l])  
        i = i + l
     return fstr 
input = ["neet","code","love","you"] 
t = encode(input)  
print(decode(t))     