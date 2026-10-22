class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 26
        for ch in s:
            temp = ord(ch) - ord('a')
            arr[temp] += 1
        for ch in t:
            temp = ord(ch) - ord('a')
            arr[temp] -= 1
        for a in arr:
            if a != 0:
                return False
        return True
