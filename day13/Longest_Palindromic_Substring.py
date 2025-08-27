class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        start, max_len = 0, 1
        def expandAroundCenter(left, right):
            nonlocal start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > max_len:
                    start = left
                    max_len = right - left + 1
                left -= 1
                right += 1
        for i in range(len(s)):
            expandAroundCenter(i, i)
            expandAroundCenter(i, i + 1)
        return s[start:start + max_len]
s = "babad"
print(Solution().longestPalindrome(s))  
