#O(n) time and space
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List[Employee], id: int) -> int:
        # Build a dictionary to map each employee ID to their corresponding Employee object.
        employee_dict = {employee.id: employee for employee in employees}
        
        # Define a recursive DFS function to get the total importance value of an employee and all their subordinates.
        def dfs(employee_id):
            employee = employee_dict[employee_id]
            total_importance = employee.importance
            for subordinate_id in employee.subordinates:
                total_importance += dfs(subordinate_id)
            return total_importance
        
        # Call the DFS function on the given employee ID.
        return dfs(id)
