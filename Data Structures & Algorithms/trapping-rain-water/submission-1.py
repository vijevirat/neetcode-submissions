class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        i = 0
        ans = 0
        max_idx = height.index(max(height))
        while i <= max_idx:
            if height[i] > height[left]:
                left = i
            ans += (height[left] - height[i])
            i += 1

        right = len(height) - 1
        j = len(height) - 1
        while j >= max_idx: 
            if height[j] > height[right]:
                right = j
            ans += (height[right] - height[j])
            j -= 1
        return ans

        