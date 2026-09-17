class Solution:
    def expand(self, s: str) -> List[str]:
        ans = [""]

        def addLetter(arr, letter):
            # if len(arr) == 0:
            #     arr.append(letter)
            # else:
            for i in range(len(arr)):
                arr[i] += letter

            return arr
    

        i = 0
        while i < len(s):
            if s[i] == '{':
                # handle expansion
                start, end = i + 1, s.find('}', i)
                options = s[start : end].split(',')
                print(f"OPTIONS: {options}")
                ansExpanded = []
                for j in range(len(options)):
                    print(f"setting currArr to {ans}")
                    currArr = ans.copy()
                    print(f"currArr = {currArr}. adding letter {options[j]} to each")
                    currArr = addLetter(currArr, options[j])
                    print(f"currArr IS NOW {currArr}")
                    ansExpanded.extend(currArr)
                
                ans = ansExpanded
                print(ans)
                i = end + 1
            else:
                ans = addLetter(ans, s[i])
                i += 1

        
        return sorted(ans)
