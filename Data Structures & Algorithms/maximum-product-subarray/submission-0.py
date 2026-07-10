class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre, suff = 1, 1
        ans = max(nums)
        l = len(nums)

        for i in range(l):
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1

            pre *= nums[i]
            suff *= nums[l - 1 - i]

            ans = max(ans, pre, suff)

        return ans
        
        
