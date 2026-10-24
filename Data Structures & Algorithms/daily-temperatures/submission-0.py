class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        length = len(temperatures)
        ans = [0]*length
        for i in range (length):
            t = temperatures[i]
            while stack and temperatures[stack[-1]] < t:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return ans
        