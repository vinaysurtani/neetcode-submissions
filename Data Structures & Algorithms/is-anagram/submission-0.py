class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = sorted([st for st in s])
        list_t = sorted([ts for ts in t])
        #print(list_s,list_t)
        return list_s==list_t