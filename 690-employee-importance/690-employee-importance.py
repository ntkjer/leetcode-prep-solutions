"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        empMap = defaultdict()
        for emp in employees:
            empMap[emp.id] = emp
        
        visit = set()
        def dfs(employee):
            if not employee:
                return 0
            if employee in visit:
                return 0
            
            visit.add(employee)
            
            curr = employee.importance
        
            subs = 0
            for sub in employee.subordinates:
                subs += dfs(empMap[sub])
            return curr + subs
        
        res = 0
        res = dfs(empMap[id])
        return res
            