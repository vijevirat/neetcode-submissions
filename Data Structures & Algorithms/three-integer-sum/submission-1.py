class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set()
        s.add(nums[0])
        ans = set()
        for i in range (1, len(nums)):
            for j in range (i+1, len(nums)):
                r =  - (nums[i] + nums[j])
                if r in s:
                    sl = [r, nums[i], nums[j]]
                    sl.sort()

                    ans.add(tuple(sl))
            s.add(nums[i])
        return list(ans)


        