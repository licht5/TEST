# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        if(m<1 or n<1):
            return -1
        # write code here
        child = [1] * n
        start=0
        num=0
        kaishi=len(child)
        while(kaishi>1):
            if(child[start%n]==0):
                start += 1
            if(child[start%n]==1 and num!=(m-1)):
                start+=1
                num+=1
            if (child[start % n]==1 and num == (m-1)):

                child[start % n]=0
                start += 1
                kaishi=kaishi-1
                num=0
        for i in range(len(child)):
            if child[i]==1:
                return i




if __name__ == '__main__':
    s=Solution()
    a=s.LastRemaining_Solution(0,0)
    print(a)