class Solution:
    def expand(self, s: str) -> List[str]:
        ans = [""]

        def addLetter(arr, letter):
            for i in range(len(arr)):
                arr[i] += letter

            return arr
    

        i = 0
        while i < len(s):
            if s[i] == '{':
                # handle expansion
                start, end = i + 1, s.find('}', i)
                options = s[start : end].split(',')
                ansExpanded = []
                for j in range(len(options)):
                    currArr = ans.copy()
                    currArr = addLetter(currArr, options[j])
                    ansExpanded.extend(currArr)
                
                ans = ansExpanded
                i = end + 1
            else:
                ans = addLetter(ans, s[i])
                i += 1

        
        return sorted(ans)
