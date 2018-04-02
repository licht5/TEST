class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        half_len=int((len(numbers)+1)/2)
        d={}
        for i in numbers:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i]=1
        for key in d:
            if d[key]>=half_len:
                return key
        return 0
if __name__ == '__main__':
    s=Solution()
    a=s.MoreThanHalfNum_Solution([4,2,1,4,2,4])
    print(a)