class Solution:
    def climbStairs(self, n: int) -> int:
        DP = [0 for _ in range(n)]

        def pick(t):
            if t == n:
                return 1
            if t > n:
                return 0
            return DP[t]
        i = n - 1
        while i >= 0:
            DP[i] = pick(i + 1) + pick(i + 2)
            i -= 1
        return DP[0]