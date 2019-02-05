class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        switcher = {'I': 1,'V': 5,'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000  }
        t = 0         
        for i in range(len(s) -1 ):
            curr = switcher[s[i]]
            nex = switcher[s[i+1]]
            if curr < nex:
                t += -curr
            else:
                t += curr
        
        t = t + switcher[s[-1]]
        return t  
