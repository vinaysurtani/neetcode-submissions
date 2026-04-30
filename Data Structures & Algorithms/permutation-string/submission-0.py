class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        s1_dict = defaultdict(int)
        for s in s1:
            s1_dict[s] += 1
        #print(s1_dict)
        s2_dict = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            #print(s2[r])
            if (r-l+1) < window:
                s2_dict[s2[r]] += 1
            elif (r-l+1) == window:
                s2_dict[s2[r]] += 1
                if s1_dict == s2_dict:
                    return True
            else:
                s2_dict[s2[l]] -= 1
                if s2_dict[s2[l]] == 0:
                    s2_dict.pop(s2[l])
                l += 1
                s2_dict[s2[r]] += 1
                if s1_dict == s2_dict:
                    return True
            #print(s2_dict)
        return False