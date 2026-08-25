class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_speed = r
        while l <= r:
            speed = l + (r - l) // 2
            if self.validSpeed(speed, piles, h):
                min_speed = min(speed, min_speed)
                r = speed - 1
            else:
                l = speed + 1
        
        return min_speed



    def validSpeed(self, speed, piles, h) -> bool:
        hours = 0
        piles_copy = piles[:]
        for p in piles:
            hours += math.ceil(float(p) / speed)
        return hours <= h