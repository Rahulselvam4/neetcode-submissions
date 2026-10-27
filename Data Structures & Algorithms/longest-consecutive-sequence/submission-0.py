class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        ans = 1
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                curr += 1
            else:
                curr = 1
            ans = max(curr, ans)
        return ans