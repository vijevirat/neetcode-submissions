class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j= 0, len(heights)-1
        left, right=i,j
        ans = 0
        while i < j:
            if heights[left] < heights[i]:
                left = i
            if heights[right] < heights[j]:
                right = j
            c = min(heights[left],heights[right]) * (right-left)
            ans = max(ans, c)
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return ans
            
        