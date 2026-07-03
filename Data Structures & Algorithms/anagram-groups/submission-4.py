class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # tuple(char array) : list of strings
        for s in strs:
            cur = [0] * 26 # new char array for each string
            for c in s:
                cur[ord(c) - ord('a')] += 1 # same as anagram method
            res[tuple(cur)].append(s) # tuple(cur) and not direct because we cant use list as key, but tuple works.
        return list(res.values()) # we only want to return the values set and dont need the keys, which is the binary stuff