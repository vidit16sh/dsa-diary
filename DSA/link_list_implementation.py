class Node: 
    def __init__(self,data,next=None): 
        self.data = data 
        self.next = next
class link_list: 
    def __init__(self): 
        self.head = None 
    def insert_element_at_being(self,data): 
        node = Node(data,self.head) 
        self.head = node 
    def insert_element_at_end(self,data): 
            it = self.head  
            while it: 
                if it.next == None: 
                   node = Node(data,None) 
                   it.next = node 
                   break
                it = it.next 
 
    def print(self): 
        if self.head is None: 
            print("the Link list is Empty") 
            return 
        it = self.head 
        ls = ''
        while it: 
              ls += str(it.data) + "-->" 
              it = it.next  
        print(ls)
l = link_list() 
l.insert_element_at_being(1) 
l.insert_element_at_being(2) 
l.insert_element_at_end(3)  
l.insert_element_at_end(4)  
l.insert_element_at_being(7)  
l.print()

                 