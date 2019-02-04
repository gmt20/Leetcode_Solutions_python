#recursive solution
class Solution:
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        final = []
        final = self.traveral(root,final)   
        return final
        
    def traveral(self,root,final):
        if root:
            if root.left:
                self.traveral(root.left,final)
            final.append(root.val)
            if root.right:
                self.traveral(root.right,final)
        
        return final
  
  #iterative solution
  class Solution:
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # using list as stack, first add all the left child nodes into stack , then pop the top element , add it to result and add the right node to stack
        final = []
        res = []
        newroot = root
     
        while newroot or final:           
            while newroot:
                final.append(newroot)
                newroot = newroot.left
            
            newroot = final.pop()
            res.append(newroot.val)
            newroot = newroot.right
            
        return res    
