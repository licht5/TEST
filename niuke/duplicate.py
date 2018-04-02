# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        d={}
        for i in numbers:
            if i in d:
                duplication.append(i)
                return True,duplication[0]
            else:
                d[i]=1
        return False
if __name__ == '__main__':
  s=Solution()
  f=[]
  a=s.duplicate([2,1,3,1,4],f)
  print(a)
