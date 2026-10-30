
import math

class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        low = 1
        high = 10**7
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            time = 0

            for i in range(len(dist)):
                if i == len(dist) - 1:
                    time += dist[i] / mid
                else:
                    time += math.ceil(dist[i] / mid)

            if time <= hour:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
