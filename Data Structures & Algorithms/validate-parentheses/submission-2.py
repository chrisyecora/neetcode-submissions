class Solution:
    def isValid(self, s: str) -> bool:
        OPENINGS = ['(', '[', '{']
        CLOSURES = [')', ']', '}']
        stack = []
        for letter in s:
            if letter in OPENINGS:
                stack.append(letter)
            elif letter in CLOSURES:
                if not len(stack): return False
                prev = stack.pop()
                for i in range(len(OPENINGS)):
                    if letter == CLOSURES[i] and prev != OPENINGS[i]:
                        return False
        
        return len(stack) == 0