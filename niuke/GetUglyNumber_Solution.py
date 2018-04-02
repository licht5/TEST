# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if (index<=0):
            return
        ugly=[1]
        uglythree=0
        uglytwo=0
        uglyfive=0
        for i in range(index-1):
            newugly=min(ugly[uglythree]*3,ugly[uglytwo]*2,ugly[uglyfive]*5)
            ugly.append(newugly)
            if(newugly%2==0):
                uglytwo+=1
            if(newugly%3==0):
                uglythree+=1
            if(newugly%5==0):
                uglyfive+=1
        return ugly[-1]
if __name__ == '__main__':
  s=Solution()
  a=s.GetUglyNumber_Solution(10)
  print(a)


