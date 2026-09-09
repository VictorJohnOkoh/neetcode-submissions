class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge sort both arrays then get the value at the middle position
        
        def merge_sort(arr1: list[int], arr2: list[int]) -> list[int]:
            left, right = 0, 0
            sorted_arr = []
            l_len, r_len = len(arr1), len(arr2)
            while left < l_len and right < r_len:
                if arr1[left] <= arr2[right]:
                    sorted_arr.append(arr1[left])
                    left += 1
                else:
                    sorted_arr.append(arr2[right])
                    right += 1
            if left == l_len:
                sorted_arr += arr2[right:]
            else:
                sorted_arr += arr1[left:]
            return sorted_arr
        merged_nums = merge_sort(nums1, nums2)
        print(merged_nums)
        mid_point = len(merged_nums) / 2
        if len(merged_nums) % 2 == 0:
            left_mid, right_mid = merged_nums[int(mid_point - 0.5)], merged_nums[int(mid_point + 0.5)]
            return ((left_mid + right_mid) / 2)
        else:
            return merged_nums[int(mid_point)]
