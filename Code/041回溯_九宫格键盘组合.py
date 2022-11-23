
if __name__ == '__main__':
    digits = "33"
    keyb = {
        '2':['a', 'b', 'c'],
        '3':['d', 'e', 'f'],
        '4':['g', 'h', 'i'],
        '5':['j', 'k', 'l'],
        '6':['m', 'n', 'o'],
        '7':['p', 'q', 'r', 's'],
        '8':['t', 'u', 'v'],
        '9':['w', 'x', 'y', 'z']
    }
    res = []
    
    def backTracking(startIndex, nowStr):
        if digits == '':
            return
        if startIndex == len(digits):
            res.append(nowStr[:])
            return
        
        for i in range(len(keyb[digits[startIndex]])):
            backTracking(startIndex + 1, nowStr + keyb[digits[startIndex]][i])         
        
    backTracking(0, "")
    print(res)







