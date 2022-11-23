
if __name__ == '__main__':
    s = "google"
    res = []
    def isPalindrome(s):
        if s == s[::-1]:
            return True
        return False
    
    def resPush(path):
        temp = []
        begin = 0
        for end in path:
            temp.append(s[begin:end + 1])
            begin = end + 1

        res.append(temp[:])
        return

    def backTracking(stratIndex, path):
        if stratIndex == len(s):
            resPush(path)
            return

        for i in range(stratIndex, len(s)):
            if isPalindrome(s[stratIndex:i + 1]):
                path.append(i)
                backTracking(i + 1, path)
                path.pop()
    

    backTracking(0, [])
    print(res)

