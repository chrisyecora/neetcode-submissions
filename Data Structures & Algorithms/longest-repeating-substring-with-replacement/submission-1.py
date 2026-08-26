class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        length = 0

        L = 0
        maxf = 0
        for R in range(len(s)):
            d[s[R]] = 1 + d.get(s[R], 0)
            maxf = max(maxf, d[s[R]])

            while (R - L + 1) - maxf > k:
                d[s[L]] -= 1
                L += 1
            
            length = max(length, R - L + 1)


        return length
            