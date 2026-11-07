class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxx = 0
        while l < r:
            h = min(heights[l], heights[r])
            maxx = max(maxx , int(h * (r - l)))
            if heights[r] >= heights[l]:
                l += 1
            else:
                r -= 1
        return maxx