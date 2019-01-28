"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        # Mark all the vertices as not visited 
       # visited = [False] * (len(self.graph)) 
  
        # Create a queue for BFS 
        queue = []
        diction = {e.id: e for e in employees}
        queue.append(diction[id])
        
        imp = 0
        while queue:
            s = queue.pop(0)
            imp = imp + s.importance
            for eid in s.subordinates:
                queue.append(diction[eid]) 
                   
        return imp
            
