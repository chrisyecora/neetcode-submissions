class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = {}
        for i in range(len(order)):
            alphabet[order[i]] = i
        

        left = 0
        right = 1
        while right < len(words):
            for i in range(len(words[left])):
                if i == len(words[right]):
                    return False
                elif alphabet[words[left][i]] > alphabet[words[right][i]]:
                    return False
                elif alphabet[words[left][i]] < alphabet[words[right][i]]:
                    break
                else:
                    # alphabet[words[left][i]] == alphabet[words[right][i]]
                    continue
            left += 1
            right += 1
        return True

