class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        merge_sort = collections.deque([i] for i in nums)
        sorted_nums = []
        arr1 = 0
        arr2 = 1

        while True:
            left = 0
            right = 0
            temp = []
            while left < len(merge_sort[arr1]) and right < len(merge_sort[arr2]):
                if merge_sort[arr1][left] < merge_sort[arr2][right]:
                    temp.append(merge_sort[arr1][left])
                    left += 1
                else:
                    temp.append(merge_sort[arr2][right])
                    right += 1
            if left < len(merge_sort[arr1]):
                temp += merge_sort[arr1][left:]
            else:
                temp += merge_sort[arr2][right:] 
            a = merge_sort.popleft()
            b = merge_sort.popleft()
            merge_sort.append(temp)
            
            if len(merge_sort[0]) == len(nums):
                sorted_nums = merge_sort[0]
                break

        for i in range(len(sorted_nums)):
            left = i + 1
            right = len(nums) - 1
            target = -(sorted_nums[i])
            while left < right:
                
                temp_sum = sorted_nums[left] + sorted_nums[right]    
                if temp_sum < target:
                    left += 1
                elif temp_sum > target:
                    right -= 1
                else:
                    if [sorted_nums[i], sorted_nums[left], sorted_nums[right]] not in res:
                        res.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1
         
        return res