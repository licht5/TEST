class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        cou=0
        for i in range(1,n+1):
            while(i/10>=0.1):
                if i%10==1:
                    cou=cou+1
                    i=i/10
                i=i/10
        return  cou
if __name__ == '__main__':
    s=Solution()
    a=s.NumberOf1Between1AndN_Solution(1)
    print(a)