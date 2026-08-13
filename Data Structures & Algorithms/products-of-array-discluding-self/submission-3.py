class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0 for i in nums]



        # First pass computes the prefix products and stores it in res
        # Second pass computes the postfix products and multiplies the prefix in res by it

    # Computed the prefix
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
             
    # Compute the postfix
        postfix = 1
        for i in range(len(nums) - 1, -1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
           