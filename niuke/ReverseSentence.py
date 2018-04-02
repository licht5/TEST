# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here

        if(len(s)<=0):
            return  ""
        a=s.split(' ')

        if(len(a)==1):
            return s
        d=[]
        for i in a:
            d.insert(0,i)
        return " ".join(d)



if __name__ == '__main__':
  s=Solution()
  a=s.ReverseSentence("I am a student.")
  print(a)