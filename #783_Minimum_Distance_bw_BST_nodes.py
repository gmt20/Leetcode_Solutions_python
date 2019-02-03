# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
   
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        arr = []
        min = 1000000;
        def inorder(root):
            if root is not None:
                inorder(root.left)
                arr.append(root.val)
                inorder(root.right)
        
        inorder(root)
        print(arr)
        first = arr[0]
        for second in arr[1:]:
            if min > abs(first - second):
                min = abs(first - second)
            first = second
            
        return min               
       
