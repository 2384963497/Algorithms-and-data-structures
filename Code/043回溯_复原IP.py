
if __name__ == '__main__':
    s = "101023"
    res = []
 
    def isValid(st):
        if int(st) > 255 or (len(st) > 1 and st[0] == '0'):
            return False
        return True
        
    def resPush(path):
        temp = ''
        begin = 0
        for end in path:
            temp = temp + s[begin:end + 1] + '.'
            begin = end + 1
        temp = temp[0:-1]
        res.append(temp)
        return

    def backTracking(stratIndex, path, le):
        if stratIndex == len(s) and le == 0:
            resPush(path)
            return
        if stratIndex > len(s):
            return
        
        for i in range(stratIndex, len(s)): # 每一段的最大长度为3 所以为起始位置 + 2 + 1
            # print(int(s[stratIndex:i + 1]))
            if isValid(s[stratIndex: i + 1]) and le >= 1:
                path.append(i)
                backTracking(i + 1, path, le - 1)
                path.pop()
            else:
                break
                
    
    backTracking(0, [], 4)
    print(res)
                
        
        






