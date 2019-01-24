class KthLargest(object):
    n = []
    k = 0
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.n = []
        self.k = k
        for i in nums:
            self.add(i)

    def add(self, val):
         
        """
        :type val: int
        :rtype: int
        """
        
        if len(self.n) < self.k:
            heapq.heappush(self.n,val)
        else:
            if val >= self.n[0]:
                heapq.heapreplace(self.n, val)
        
                   
       
        return self.n[0]        
      
