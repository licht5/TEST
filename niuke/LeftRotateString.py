# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        # s=list(s)
        if not s:
            return []
        k=n%len(s)
        return  s[k:]+s[:k]
if __name__ == '__main__':
    s=Solution()
    a=s.LeftRotateString("tfhxq",3)
    print(a)