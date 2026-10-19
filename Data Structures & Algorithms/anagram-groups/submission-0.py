class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        for s in strs:
            st = ''.join(sorted(s))
            ana.setdefault(st, []).append(s)
        return list(ana.values())
        