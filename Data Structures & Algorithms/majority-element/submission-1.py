class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        maxx = nums[0]
        for n in nums:
            if n == maxx:
                count += 1
            else:
                count -= 1
                if count == 0:
                    maxx = n
                    count += 1
        return maxx