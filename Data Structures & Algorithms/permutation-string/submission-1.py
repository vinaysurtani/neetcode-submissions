class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1c, s2c = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1c[ord(s1[i]) - ord('a')] += 1
            s2c[ord(s2[i]) - ord('a')] += 1
        matches = 0
        for i in range(26):
            matches += (1 if s1c[i]==s2c[i] else 0) #initial match made for the first few values
        l = 0
        for r in range(len(s1),len(s2)):
            if matches == 26: #checks matches at every loop
                return True
            index = ord(s2[r]) - ord('a')
            s2c[index] += 1 #value added
            if s1c[index] == s2c[index]: #check if changing this count has caused a match
                matches += 1
            elif s1c[index] + 1 == s2c[index]: #this is a case where it was a match and now changing it has caused it to not match
                matches -= 1
            index = ord(s2[l]) - ord('a')
            s2c[index] -= 1 #value to remove
            if s1c[index] == s2c[index]: #checks if removing this value causes a match
                matches += 1
            elif s1c[index] -1 == s2c[index]: #it was matching earlier but not its not
                matches -= 1
            l += 1 # very important step
        return matches == 26 # checking here as last case of check is skipped