class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs = (re.sub(r'[^a-zA-Z0-9]', '', s)).lower()
        return cs == cs[::-1]
        