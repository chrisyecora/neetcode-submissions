class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def validateCapacity(c):
            currWeight = 0
            i = 0
            numDays = 1
            while i < len(weights):
                if weights[i] + currWeight <= c:
                    currWeight += weights[i]
                else:
                    numDays += 1
                    currWeight = weights[i]
                i += 1
            return numDays <= days

    
        lower = max(weights)
        upper = sum(weights)
        cap = upper
        while lower <= upper:
            currCap = lower + (upper - lower) // 2
            if validateCapacity(currCap):
                upper = currCap - 1
                cap = min(cap, currCap)
            else:
                lower = currCap + 1
            

        return cap
