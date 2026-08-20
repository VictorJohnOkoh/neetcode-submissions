class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water_vol = 0
        # 2 pointers at the start and end of the list
        l = 0
        r = len(heights) - 1

        # Look through the list and find the area between the pointers and compare ti to teh curent max area
        while l < r:
            w = r - l
            area = min(heights[l], heights[r])
            water_vol = max(w * area, water_vol)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return water_vol