class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
         
        final = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        last = -sys.maxint
        i = 0
        j = 0
        k = 0
        while i < len(nums1) and j < len(nums2):           
            if nums1[i] == nums2[j] and  nums1[i] != last:
                final.append(nums1[i])
                last = nums1[i]
                i = i+ 1
                j = j +1
                
            elif nums1[i] < nums2[j]:
                i = i + 1
            else:
                j = j + 1
       
   
        return final
