class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            #print(f'res right now is {res}')
            cur = ""
            for s in strs:
                if s == "" or i >= len(s):
                    return res
                #print(f'str right now is {s[i]}')
                if cur == "":
                    cur += s[i]
                elif cur == s[i]:
                    continue
                else:
                    return res
            res += cur
            #print(f'cur = {cur} and res = {res}')
        return res