s = "abcdef"
s = "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"

DP = [[-1 for i in range(len(s))] for j in range(len(s))]

for i in range(len(s)):
    DP[i][i] = 1
    if i == len(s) - 1:
        break
    DP[i][i + 1] = 2 if s[i] == s[i + 1] else 1

for i in range(len(s) - 2, -1, -1): # 从最后一行开始填
    for j in range(i + 2, len(s)):
        r2 = DP[i][j - 1]
        r3 = DP[i + 1][j]
        DP[i][j] = max(r3, r2)
        if s[i] == s[j]:
            DP[i][j] = max(DP[i][j], DP[i + 1][j - 1] + 2)

print(DP[0][len(s) - 1])

