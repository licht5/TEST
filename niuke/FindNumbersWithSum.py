# -*- coding:utf-8 -*-
class Solution:
    def hahh(self,l):
        if (len(l)>1):
            n=0
            su=1
            for f in l[0]:
                su=su*f
            for k in range(len(l)):
                tem = 1
                for o in l[k]:
                    tem=tem*o
                if(tem<su):
                    su=tem
                    n=k
            return l[n]
        if(len(l)<=0):
            return []
        else:
            return l[0]
    def FindNumbersWithSum(self, array, tsum):
        l = []
        for i in range(len(array)):
            d = []
            for j in range(i+1, len(array)):
                if(array[i]+array[j]==tsum):
                    d.append(array[i])
                    d.append(array[j])
                    l.append(d)
        return  self.hahh(l)



if __name__ == '__main__':
  s=Solution()
  a=s.FindNumbersWithSum([1,2,4,7,11,16],10)
  print(a)

