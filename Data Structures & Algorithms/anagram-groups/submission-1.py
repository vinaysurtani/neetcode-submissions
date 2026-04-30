class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            key = tuple(count)
            if key not in dct:
                dct[key] = []
            dct[tuple(count)].append(s)
        return (list(dct.values()))