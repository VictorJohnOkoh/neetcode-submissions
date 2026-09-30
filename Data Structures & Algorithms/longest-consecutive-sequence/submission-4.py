class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        sorted_nums = sorted(nums)
 
        longest = 0
        curr = 0
        prev = sorted_nums[0]-1 
        for i in range(len(nums)):
            if prev == sorted_nums[i]:
                continue
            elif prev + 1 == sorted_nums[i]:
                prev = sorted_nums[i]
                curr += 1
                if curr > longest: longest = curr
            else:
                curr = 1
                prev = sorted_nums[i]
          
        return longest
