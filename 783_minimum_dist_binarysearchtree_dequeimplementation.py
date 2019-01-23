class Solution(object):
    def __init__(self):
        self.s = collections.deque()

    def minDiffInBST(self, root):
        
        def go(root, minv):
            if not root: return minv
            minv = go(root.left, minv)
            if self.s:
                temp = self.s.pop()
                self.s.append(temp)
                if minv > root.val - temp:
                    minv = root.val - temp
            self.s.append(root.val)
            minv = go(root.right, minv)
            return minv
        return go(root, float('inf'))
        
