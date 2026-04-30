class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            val = f'{len(s)}#{s}'
            res.append(val)
        encoded = ''.join(res)
        return encoded


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            wordlen = ''
            while s[j] != '#':
                wordlen += s[j]
                j += 1
            #print(f'wordlen is {wordlen}')
            val = int(wordlen)
            #print(f'val is {val}')
            res.append(s[j+1:j+1+val])
            #print(res)
            i = j + 1 + int(wordlen)
        #print(res)
        return res
