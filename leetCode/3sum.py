class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer = []
        nums.sort()
        N = len(nums)
        
        for i in range(N):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = N-1

            while left<right:
                first  = nums[i]
                second = nums[left]
                thrid = nums[right]
                if first+second+thrid == 0:
                    answer.append([first,second,thrid])
                    while left<right and nums[left] == nums[left+1]:
                        left+=1
                    while left<right and nums[right] == nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif first+second+thrid<0:
                    left+=1
                else:
                    right-=1
        
        return answer

Solution.threeSum(Solution, [-1,0,1,2,-1,-4])