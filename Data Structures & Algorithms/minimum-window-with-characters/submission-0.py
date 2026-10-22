class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = {}
        for i in t:
            t_count[i] = t_count.setdefault(i, 0) + 1
        ans = ""
        ans_length = len(s) + 1
        window = {}
        found = 0
        i,j = 0,0
        while j < len(s):
            window[s[j]] = window.setdefault(s[j], 0) + 1
            if s[j] in t_count and window[s[j]] == t_count[s[j]]:
                found+=1
            while i<=j and found == len(t_count):
                if ans_length > (j-i+1):
                    ans = s[i:j+1]
                    ans_length = j-i+1
                left = s[i]
                window[left]-=1
                if left in t_count and window[left] < t_count[left]:
                    found-=1
                i+=1
            j+=1
        return ans





