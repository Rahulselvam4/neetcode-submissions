class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            if nums[i] in map:
                map[nums[i]] += 1
            else:
                map[nums[i]] = 1
        list = []
        ans = []
        for key , v in map.items():
            list.append([v , key])
        list.sort()
        while k > 0:
            k -= 1
            ans.append(list.pop()[1])
            
        return ans