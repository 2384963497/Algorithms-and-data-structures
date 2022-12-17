s = "aaaaaaa"
wordDict = ["aaaa","aaa"]

DP = [False for _ in range(len(s) + 1)]
DP[0] = True

for i in range(1, len(s) + 1):
    for w in wordDict:
        if w == s[i - len(w):i] and DP[i - len(w)]:
            DP[i] = True
            break
print(DP[-1])