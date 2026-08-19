class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []        
        nums.sort()

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            target = -(nums[i])
            while left < right:
                
                temp_sum = nums[left] + nums[right]    
                if temp_sum < target:
                    left += 1
                elif temp_sum > target:
                    right -= 1
                else:
                    if [nums[i], nums[left], nums[right]] not in res:
                        res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1         
        return res
                
                        

        
            