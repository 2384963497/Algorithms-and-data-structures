# s = "abcdef"
s = "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"


tMap = {}

def tryFunc(i, j):
    if tMap.get(s[i:j+1]) != None:
        return tMap[s[i:j+1]]
    if i == j:
        tMap[s[i:j+1]] = 1
        return tMap[s[i:j+1]]
    elif i + 1 == j:
        if s[i] == s[j]:
            tMap[s[i:j+1]] = 2
            return tMap[s[i:j+1]]
        else:
            tMap[s[i:j+1]] = 1
            return tMap[s[i:j+1]]
    
    
    r0 = 0
    if s[i] == s[j]:
        r0 = tryFunc(i + 1, j - 1) + 2
    r3 = tryFunc(i + 1, j - 1)
    r1 = tryFunc(i + 1, j)
    r2 = tryFunc(i, j - 1)
    tMap[s[i:j+1]] = max(r1, r2, r0, r3)
    return tMap[s[i:j+1]]
    


print(tryFunc(0, len(s) - 1))



