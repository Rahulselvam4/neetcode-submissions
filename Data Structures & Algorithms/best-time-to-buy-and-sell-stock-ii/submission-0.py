class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minn = float('inf')
        for p in prices:
            minn = min(p,minn)
            if p > minn:
                ans += p - minn
                minn = p

        return ans