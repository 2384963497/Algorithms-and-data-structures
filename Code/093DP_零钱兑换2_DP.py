class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        DP = [0 for j in range(amount + 1)]
        DP[0] = 1

        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                DP[j] += DP[j - coins[i]]

        return DP[amount]