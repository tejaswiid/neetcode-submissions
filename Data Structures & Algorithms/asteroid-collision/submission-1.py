class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        for a in asteroids:
        
            proc = True
            while proc and stack and a < 0 and stack[-1] > 0 :
                sa, sta = abs(a), abs(stack[-1])
                if sa > sta:
                    stack.pop()
                elif sa == sta:
                    proc = False
                    stack.pop()
                else:
                    proc = False
            if proc: stack.append(a)
    
               
        return stack
                    
                        
                
            