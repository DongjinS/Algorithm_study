class Solution:
    # use two pointer
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_left,max_right = height[left], height[right]
        total = 0
        
        while left<right:
            max_left = max(max_left,height[left])
            max_right= max(max_right, height[right])
            
            if max_left<=max_right:
                total+=max_left-height[left]
                left+=1
            else:
                total+=max_right-height[right]
                right-=1
                
        return total

    #use stack
    def trap2(self, height: List[int]) -> int:
        stack = []
        total = 0
        max_height = 0
        for i in range(len(height)):
            if max_height<height[i]:
                while stack and height[stack[-1]]<height[i]:
                    top = stack.pop()
                    if not stack: break
                    dist = i-stack[-1]-1
                    amount = min(height[i],height[stack[-1]])-height[top]
                    total += dist*amount

            stack.append(i)

        return total
        
        