# -*- coding:utf-8 -*-
class Solution:
    def findpath(self,x,y):
        san=[[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]
        N=len(san)
        maxsum=[]
        for i in range(N):
            s=[0]*(i+1)
            maxsum.append(s)
        for i in range(N-1,-1,-1):
            for j in range(i,-1,-1):
                if(i==N-1):
                    maxsum[i][j] = san[i][j]
                else:
                    s1 = san[i][j] + maxsum[i+1][j]
                    s2 = san[i][j] + maxsum[i + 1][j+1]
                    maxsum[i][j]=max(s1,s2)
        return  maxsum[x][y]

if __name__ == '__main__':
  s=Solution()
  a=s.findpath(0,0)
  print(a)
