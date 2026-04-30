class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            m = (left + right) // 2
            total = 0
            for num in piles:
                if num % m == 0:
                    total += num // m
                else:
                    total += (num // m) + 1
            if total <= h:
                right = m - 1
            else:
                left = m + 1
            
        return left