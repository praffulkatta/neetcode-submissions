class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        

        stack = []

        for a in asteroids:

            while a < 0 and stack and stack[-1] > 0:

                if  stack[-1] < -a:
                    stack.pop()
                elif stack[-1] == -a:
                    stack.pop()
                
            stack.append(a)
        
        return stack
        