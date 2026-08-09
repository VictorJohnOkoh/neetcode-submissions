class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        for n in nums:
            if target - nums[i] in nums:
                while True:
                    if nums[i] + nums[j] != target:
                        j -= 1
                    else:
                        return [i, j]
            elif target - nums[j] in nums:
                while True:
                    if nums[j] + nums[i] != target:
                        i += 1
                    else:
                        return [i, j]
            else:
                i += 1
                j -= 1