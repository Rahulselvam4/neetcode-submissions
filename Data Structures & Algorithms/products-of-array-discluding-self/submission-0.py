class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        first = [0] * len(nums)
        second = [0] * len(nums)
        first[0] = 1
        second[len(nums) - 1] = 1
        for i in range(1,len(nums)):
            first[i] = nums[i - 1] * first[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            second[i] = nums[i + 1] * second[i + 1]
        for i in range(len(nums)):
            first[i] = second[i] * first[i]
        return first