class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count1 = count0 = count2 = i = 0
        for n in nums:
            if n == 0:
                count0 += 1
            elif n == 1:
                count1 += 1
            else:
                count2 += 1
        while count0 > 0 and i < len(nums):
            nums[i] = 0
            count0 -= 1
            i += 1
        while count1 > 0 and i < len(nums):
            nums[i] = 1
            count1 -= 1
            i+= 1
        while count2 > 0 and i < len(nums):
            nums[i] = 2
            count2 -= 1
            i += 1

        