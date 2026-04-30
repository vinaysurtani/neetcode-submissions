class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            wordlen = int(s[i:j])
            #print(wordlen)
            res.append(s[j + 1:j + 1 + wordlen])
            #print(res)
            i = j + 1 + wordlen
        return res