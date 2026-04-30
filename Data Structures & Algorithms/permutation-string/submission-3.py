class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count_s1 = [0] * 26
        count_s2 = [0] * 26
        matches = 0
        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_s2[ord(s2[i]) - ord('a')] += 1
        for i in range(26):
            matches += (1 if count_s1[i] == count_s2[i] else 0)
        l = 0 
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            count_s2[index] += 1
            if count_s1[index] == count_s2[index]: #if it currently matches
                matches += 1
            elif count_s1[index] + 1 == count_s2[index]: #if it matched before, that means s1_count + 1 will match now, which is not the case now
                matches -= 1

            index = ord(s2[l]) - ord('a')
            count_s2[index] -= 1
            if count_s1[index] == count_s2[index]:
                matches += 1
            elif count_s1[index] - 1 == count_s2[index]: #if it matched before, that means if we reduce count_s1 value by one, it will be equal as before, which is not the case now
                matches -= 1
            l += 1
        return matches == 26