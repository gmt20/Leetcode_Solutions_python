class Solution:
    def countBits(self, num: 'int') -> 'List[int]':
      
        if num == 0:
            return [0]
        if num == 1:
            return [0, 1]
        ret = [0, 1]
        for i in range(2, num+1):
            
            ret.append(ret[i//2] + (i  & 1))
            
        
                       
        return ret
