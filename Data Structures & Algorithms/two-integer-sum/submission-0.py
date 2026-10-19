class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}
        for i in range (0, len(nums)):
            req = target - nums[i]
            if req in x:
                return [x[req], i]
            x[nums[i]] = i

        