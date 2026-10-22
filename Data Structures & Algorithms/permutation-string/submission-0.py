class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = [0]*26
        for i in s1:
            freq[ord(i)-97]+=1
        for i in range (0, len(s2)):
            s = s2[i:i+len(s1)]
            pfreq = [0]*26
            for j in s:
                pfreq[ord(j)-97]+=1
            k = 0
            while k < 26 and pfreq[k] == freq[k]:
                k+=1
            if k == 26:
                return True
        return False
            
        