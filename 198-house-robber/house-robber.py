class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if (n == 0):
            return 0
        if n == 1:
            return nums[0]

        prev2 = nums[0]
        prev = max(nums[0], nums[1])

        for i in range(2, n):
            curr = max(nums[i] + prev2, prev)
            prev2 = prev
            prev = curr

        return prev