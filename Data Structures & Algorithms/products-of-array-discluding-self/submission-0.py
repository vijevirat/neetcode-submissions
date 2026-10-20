class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = math.prod(nums)
        zeros = nums.count(0)
        rest = 0 if zeros > 1 else math.prod(i for i in nums if i!=0)
        return [p//i if i!=0 else rest for i in nums]
         