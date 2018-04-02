# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        B = []
        for i in range(len(A)):
            tem = 1
            for j in range(len(A)):
                if (j != i):
                    tem = tem * A[j]
            B.append(tem)
        return  B
if __name__ == '__main__':
    s=Solution()
    a=s.multiply([4,2,1,4,2,4])
    print(a)
