class Solution:
    def minWindow(self, s: str, t: str) -> str:
        substring = {}
        for lett in t:
            substring[lett] = 1 + substring.get(lett, 0)

        l = 0
        seen = {}
        minLength = float('inf')
        indices = [-1, -1]
        have = 0
        need = len(substring.keys())
        for r in range(len(s)):
            # process
            if s[r] in t:
                seen[s[r]] = 1 + seen.get(s[r], 0)
                if seen[s[r]] == substring[s[r]]:
                    have += 1

            # check condition
            while have == need:
                # save progress
                if (r - l + 1) < minLength:
                    minLength = r - l + 1
                    indices = [l, r]
                # shrink
                if s[l] in seen:
                    seen[s[l]] -= 1
                    if seen[s[l]] < substring[s[l]]:
                        have -= 1
                l += 1
            
        if minLength < float('inf'):
            return s[indices[0]:indices[1] + 1]

        return ""
                
                    
        
