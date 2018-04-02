# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        lenth=len(num)
        if (lenth<=0 or lenth<size):
            return
        d=[]
        for i in range(0,lenth-size+1):
            s=[]
            for j in range(size):
                s.append(num[i+j])
            a=max(s)
            d.append(a)
        return d
if __name__ == '__main__':
    s=Solution()
    a=s.maxInWindows([4,2,1,4,2,4],2)
    print(a)