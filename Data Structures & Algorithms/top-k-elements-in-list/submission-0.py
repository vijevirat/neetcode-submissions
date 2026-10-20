class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for i in nums:
            cnt[i] = cnt.setdefault(i, 0) + 1
        sorted_cnt = sorted(cnt, key=cnt.get, reverse=True)
        return sorted_cnt[:k]
        