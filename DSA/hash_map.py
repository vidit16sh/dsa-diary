class Hash_map: 
    def __init__(self): 
        self.max = 100 
        self.arr = [None for i in range(self.max)] 
    def hash(self,str): 
        h = 0 
        for i in str: 
            h += ord(i) 
        h = h % 100 
        print(h) 
        return h 
    def insert_element(self,key,value): 
        index = self.hash(key) 
        self.arr[index] = value 
        print(self.arr) 
sol = Hash_map() 
sol.insert_element("hello","world") 
sol.insert_element("hey","vidit")