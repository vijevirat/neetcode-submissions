class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        idx = []
        for i in range (len(nums)):
            while idx and nums[idx[-1]] <= nums[i]:
                idx.pop()
            idx.append(i)
            if idx[0] < i-k+1:
                idx.pop(0)
            if i>=k-1:
                ans.append(nums[idx[0]])
        return ans