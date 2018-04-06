# -*- coding:utf-8 -*-
class Solution:
    def findpath(self,x,y):
        san=[[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]
        N=len(san)
        if(x==N-1):
            return san[x][y]
        else:
            return max(self.findpath(x+1,y)+san[x][y],self.findpath(x+1,y+1)+san[x][y])



if __name__ == '__main__':
  s=Solution()
  a=s.findpath(0,0)
  print(a)
