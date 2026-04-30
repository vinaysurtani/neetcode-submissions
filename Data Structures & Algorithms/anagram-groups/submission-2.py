class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            if tuple(count) not in hm.keys():
                hm[tuple(count)] = []
            hm[tuple(count)].append(s)
        #print(hm)
        return list(hm.values())