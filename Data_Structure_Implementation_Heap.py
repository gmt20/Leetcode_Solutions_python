class minheap:
    
    def __init__(self):
        self.heaplist = []
        self.size = 0
    def find_pos(self, length):
        # children of a node are located at 2i and 2i + 1 positions
        # compare child with parent to ensure head order.
        # do this recursively till there is no anomalous node in the tree that disatisfy heap          
        while length//2:
            parent = (length)//2 - 1
            child = length - 1
            if self.heaplist[parent] > self.heaplist[child]:
                # swap child with parent
                temp = self.heaplist[parent] 
                self.heaplist[parent]  = self.heaplist[child]
                self.heaplist[child]= temp
                length = length//2
            else: return
                
    def add(self, data):
        self.heaplist.append(data)
        self.size += 1
        self.find_pos(self.size)
    
    def printheap(self):
        print(self.heaplist)
    
    def peek(self):
        # this returns the min value without deleting it
        return self.heaplist[0]
    
    def pop(self):
        # this returns the min value and delete it from heap
        end = self.size - 1
        self.size = self.size - 1
        valtoret = self.heaplist[0]
        self.heaplist[0] = self.heaplist[end]
        end -= 1
        i = 0
        while i < end:
            minimum = i
            
            if i * 2 <= end:
                if self.heaplist[minimum] > self.heaplist[i * 2]:
                    minimum =  i * 2
            if i * 2 + 1 <= end:
                if self.heaplist[minimum] > self.heaplist[i * 2 +1]:
                    minimum = i * 2 +1
            #swap minimum with root
            if minimum == i: break
            temp = self.heaplist[i]
            self.heaplist[i] = self.heaplist[minimum]
            self.heaplist[minimum] = temp
            i = minimum
    
        return valtoret
                
         
    def heapsort(self):     
        ret = []
        while self.size > 0:
            ret.append(self.pop())
            
        
        return ret
