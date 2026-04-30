class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for a in strs:
            s += a + "-"
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        a = s.split('-')
        print(a[:-1])
        return a[:-1]
