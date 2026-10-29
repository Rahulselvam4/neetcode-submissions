class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        map = {}
        for n in nums:
            if n in map:
                map[n] = map[n] + 1
            else:
                map[n] = 1
        ans = []
        for k,v in map.items():
            if v > leng/3:
                ans.append(k)
        return ans