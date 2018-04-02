# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        cout=0
        s=sorted(numbers)
        for i in range(len(s)):
            if(s[i]==0):
                cout+=1
        for k in range(cout):
            del (s[0])
        num=0
        for j in range(1,len(s)):
            if(s[j]==s[j-1]):
                return False
            else:
                num=num+(s[j]-s[j-1]-1)
        if num>cout:
            return False
        if num<=cout:
            return True





if __name__ == '__main__':
    s=Solution()
    a=s.IsContinuous([1,3,0,5,0])
    print(a)