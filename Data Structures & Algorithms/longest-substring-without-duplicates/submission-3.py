class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        i = 0
        idx = {}
        ans = 0
        while i < len(s):
            if s[i] in idx:
                ans = max(ans, i - left)
                left = max(left, idx[s[i]] + 1)
            idx[s[i]] = i
            i+=1
            if i == len(s):
                ans = max(ans, i-left)
        return ans