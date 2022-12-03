class Solution:
    def numDecodings(self, s: str) -> int:
        tMap = [-1 for _ in range(len(s) + 1)]

        tMap[-1] = 1

        for i in range(len(s) - 1, -1, -1): # 从右往左填表
            if s[i] == '0':
                tMap[i] = 0
                continue
            r1 = tMap[i + 1]
            r2 = 0 
            if i < len(s) - 1 and int(s[i:i + 2]) <= 26:
                r2 = tMap[i + 2]
            tMap[i] = r1 + r2

        return tMap[0]