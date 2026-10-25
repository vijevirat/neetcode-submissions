class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(speed) == 0:
            return 0
        dic = {position[i]:speed[i] for i in range(len(speed))}
        ans = 0
        time = float('-inf')
        for i in sorted(dic, reverse=True):
            t = (target - i) / dic[i]
            if t > time:
                ans+=1
                time = t
            
        return ans
