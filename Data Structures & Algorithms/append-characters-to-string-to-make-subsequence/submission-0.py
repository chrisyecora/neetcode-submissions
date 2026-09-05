class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i_s = 0
        j_t = 0
        while i_s < len(s) and j_t < len(t):
            if s[i_s] == t[j_t]:
                j_t += 1
            i_s += 1

        return len(t) - j_t