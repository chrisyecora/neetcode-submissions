class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letters_s = {}
        letters_t = {}

        for i in range(len(s)):
            letters_s[s[i]] = 1 + letters_s.get(s[i], 0)
            letters_t[t[i]] = 1 + letters_t.get(t[i], 0)

        return letters_s == letters_t