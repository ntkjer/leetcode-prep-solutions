class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleet = [[p,s] for p,s in zip(position, speed)]
        fleet.sort()
        stack = []
        
        for i in reversed(range(len(fleet))):
            p, s = fleet[i]
            curr = (target - p) / s
            stack.append(curr)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)