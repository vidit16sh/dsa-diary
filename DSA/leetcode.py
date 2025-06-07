class MedianFinder(object):

    def __init__(self):
        self.nums = []
    def addNum(self, num):
        self.nums.append(num)
    
    def findMedian(self): 
        
        if len(self.nums)%2 == 0:  
            return ((self.nums[(len(self.nums)//2)-1]+self.nums[len(self.nums)//2])/2)    
        else: 
            return float(self.nums[(len(self.nums) + 1) // 2 - 1])
medianFinder = MedianFinder() 
medianFinder.addNum(1);     
medianFinder.addNum(2);    
print(medianFinder.findMedian()); 
medianFinder.addNum(3);    
medianFinder.findMedian();    
