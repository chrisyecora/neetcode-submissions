class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded
    def decode(self, s: str) -> List[str]:
        pointer = 0
        words = []
        print(s)
        while pointer < len(s):
            delim = s.find("#", pointer)
            print(delim)
            length = int(s[pointer:delim])
            words.append(s[delim + 1 : delim + length + 1])
            pointer = delim + length + 1
        return words

