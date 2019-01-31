class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        num = 0
        for s in S:
            if s in J:
                num = num + 1
                    
                    
        return num
        
 class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
                       
        return sum(s in J for s in S)
   class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
                       
        return sum(J.count(s) for s in S)
