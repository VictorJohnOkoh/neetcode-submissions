class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        def bin_search(arr: list[int], target: int):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
        
        for row in matrix:
            if row[-1] >= target:
                return bin_search(row, target)
        return False