class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
       
        largest,  currsum = nums[0], nums[0]
       
        for i in range(1,len(nums)):
            if nums[i] + currsum >= nums[i]:
                currsum = nums[i] + currsum
            else:
                currsum = nums[i]
            if largest < currsum:
                largest = currsum
                
        
        return largest
            
