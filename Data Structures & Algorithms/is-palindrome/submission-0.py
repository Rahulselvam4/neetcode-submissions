class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        for word in s:
            if word.isalnum():
                ss += word.lower()
        return ss == ss[::-1]