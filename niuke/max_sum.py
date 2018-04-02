class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array) < 1:
            return
        maxs = -1
        cur = 0
        for i in array:
            if cur<= 0:
                cur = i
            else:
                cur = cur + i
            if maxs < cur:
                maxs = cur
        return maxs
if __name__ == '__main__':
    s=Solution()
    a=s.FindGreatestSumOfSubArray([1,-2,3,10,-4,7,2,-5])
    print(a)