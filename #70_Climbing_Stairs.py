class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        
        memo = {}
        
        def t(no):
            
            if no <= 2:
                memo[no]= no
                return memo[no]
            else:
                if no-2 not in memo:
                    memo[no -2] = t(no-2)
                if no -1 not  in memo:
                    memo[no -1] = t(no-1)
                
                memo[no]=  memo[no -2] + memo[no -1]
                return memo[no]
       
        
        return t(n)
        
