class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        l = 0
        for r in range(1, len(strs)):
            i = 0
            while i < len(strs[r]) and i < len(prefix) and strs[r][i] == prefix[i]:
                i+=1
            prefix = prefix[:i]

        return prefix
        