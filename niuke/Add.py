# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        while(num2!=0):
            n=num1^num2
            carry=(num1&num2)<<1
            num1=n
            num2=carry
        return num1
if __name__ == '__main__':
  s=Solution()
  a=s.Add(2,10)
  print(a)
