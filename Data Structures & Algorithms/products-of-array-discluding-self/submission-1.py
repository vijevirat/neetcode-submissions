class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0]*len(nums)
        p = math.prod(nums)
        rest = math.prod(i for i in nums if i!=0)
        return [p//i if i!=0 else rest for i in nums]
         