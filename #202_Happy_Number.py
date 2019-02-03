class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dic = {}
        def sumofsquare(num):
            temp = 0
            while num:
                m = num%10
                temp = temp  + m * m
                num = num//10
                
            return temp
        
        while n != 1:
            n = sumofsquare(n)
            if n in dic: return False
            else:
                dic[n] = 0
                    
                    
        return True  
