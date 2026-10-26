class Solution:
    def search(self, nums: List[int], target: int) -> int:
        j = len(nums)-1
        i = 0
        while i <= j:
            m = (i+j)//2
            if nums[m] == target:
                return m
            if nums[m] > target:
                j = m-1
            else:
                i = m+1
        return -1