class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i,j=0,0
        freq = [0]*26
        max_freq = 0
        ans = 0
        while j < len(s) and i < len(s):
            freq[ord(s[j])-65]+=1
            max_freq = max(max_freq, freq[ord(s[j])-65])
            remaining = sum(freq) - max_freq
            if remaining > k:
                freq[ord(s[i])-65]-=1
                i+=1
            else:
                ans = max(ans, j-i+1)
            j+=1
        return ans

